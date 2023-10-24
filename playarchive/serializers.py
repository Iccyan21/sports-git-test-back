from rest_framework import serializers
from .models import Archive, Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'video')
        
class ArchiveSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    
    class Meta:
        model = Archive
        fields = ('title', 'subtitle', 'description', 'movies')
    
    #ここで変換しないと、エラーが出る
    def to_internal_value(self, data):
        movies_data = []
        index = 0
        while f"movies[{index}].title" in data:
            movie_data = {
                "title": data.get(f"movies[{index}].title"),
                "video": data.get(f"movies[{index}].video")
            }
            movies_data.append(movie_data)
            index += 1
        return super().to_internal_value({
            "title": data.get("title"),
            "subtitle": data.get("subtitle"),
            "description": data.get("description"),
            "movies": movies_data
        })
