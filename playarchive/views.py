from django.shortcuts import render
from rest_framework import status, views
from .models import Archive, Movie
from .serializers import ArchiveSerializer, MovieSerializer
from rest_framework.response import Response
from django.db import transaction
from django.shortcuts import get_object_or_404

# Archive表示
class ArchiveViewSet(views.APIView):
    def get_queryset(self):
        return Archive.objects.all()
    
    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        serializer = ArchiveSerializer(posts, many=True)
        return Response(serializer.data)


class ArchiveCreateView(views.APIView):
    def post(self, request):
        serializer = ArchiveSerializer(data=request.data)
        if serializer.is_valid():
            archive_data = serializer.validated_data
            archive = Archive.objects.create(
                title=archive_data['title'],
                subtitle=archive_data['subtitle'],
                description=archive_data['description']
            )
            for movie_data in archive_data['movies']:
                Movie.objects.create(archive=archive, **movie_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#Archive詳細
class ArchiveByTitleAPI(views.APIView):
    
    def get(self, request, title):
        # Archiveのオブジェクトをtitleで取得
        archive = get_object_or_404(Archive, title=title)

        # Serializerを使用してデータを変換
        serializer = ArchiveSerializer(archive)
        
        return Response(serializer.data)

    

#Archive編集
class ArchiveEditAPIView(views.APIView):
    
    def get_object(self, title):
        try:
            return Archive.objects.get(title=title)
        except Archive.DoesNotExist:
            return None
        
    def get(self, request, title):
        archive = self.get_object(title)
        if archive is None:
            return Response({"error": "Archive not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ArchiveSerializer(archive)
        return Response(serializer.data)

    def put(self, request, title):
        archive = self.get_object(title)
        if archive is None:
            return Response({"error": "Archive not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ArchiveSerializer(archive, data=request.data)
        
        if serializer.is_valid():
            archive_data = serializer.validated_data
            archive.title = archive_data['title']
            archive.subtitle = archive_data['subtitle']
            archive.description = archive_data['description']
            archive.save()

            # 既存のMovieオブジェクトをキャッシュしておく
            existing_movies = {movie.title: movie for movie in Movie.objects.filter(archive=archive)}

            for movie_data in archive_data['movies']:
                title = movie_data.get('title')
                if title in existing_movies:
                    # 既存のMovieオブジェクトを更新
                    movie = existing_movies[title]
                    for key, value in movie_data.items():
                        setattr(movie, key, value)
                    movie.save()
                    del existing_movies[title]  # 更新されたMovieはキャッシュから削除
                else:
                    # 新しいMovieオブジェクトを作成
                    Movie.objects.create(archive=archive, **movie_data)

            # 未使用の既存のMovieオブジェクトを削除
            for movie in existing_movies.values():
                movie.delete()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Archive削除
class ArchiveDeleteAPIView(views.APIView):
    
    def get_object(self, title):
        try:
            return Archive.objects.get(title=title)
        except Archive.DoesNotExist:
            return None
        
    def delete(self, request, title):
        archive = self.get_object(title)
        if archive is None:
            return Response({"error": "Archive not found"}, status=status.HTTP_404_NOT_FOUND)

        # 必要に応じて、関連するMovieデータも削除することができます。
        # Movie.objects.filter(archive=archive).delete()
        
        archive.delete()
        return Response({"message": "Archive deleted successfully"}, status=status.HTTP_200_OK)
    
class MovieCreateView(views.APIView):
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)