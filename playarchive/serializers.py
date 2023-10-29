from rest_framework import serializers
from .models import Archive, Movie

class CustomFileField(serializers.FileField):
    def to_internal_value(self, data):
        # 既存のファイルのパスの場合
        if isinstance(data, str) and data.startswith('/media/'):
            return data
        # それ以外の場合、デフォルトの処理を行う
        return super().to_internal_value(data)


class MovieSerializer(serializers.ModelSerializer):
    video = CustomFileField(max_length=100)
    class Meta:
        model = Movie
        fields = ('title', 'video')
    
    def update(self, instance, validated_data):
        video_file = validated_data.get('video', None)
        
        # 新しいvideoファイルが提供されているかどうかを確認
        if video_file:
            instance.video = video_file

        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


        
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
        

# serializers.py
