from rest_framework import serializers
from .models import Archive, Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'video')
        
class ArchiveSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Archive
        fields = ('title', 'subtitle', 'description', 'movies')
