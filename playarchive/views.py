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


#Archive作成
class ArchiveCreateView(views.APIView):
    def post(self, request):
        serializer = ArchiveSerializer(data=request.data)
        if serializer.is_valid():
            # Archiveのインスタンスを初期化してからsave()
            archive = Archive(**serializer.validated_data)
            archive.save()
            movies_data = request.data.get('movies', [])
            for movie_data in movies_data:

                # Movieのインスタンスを初期化してからsave()
                movie = Movie(archive=archive, **movie_data)
 
                movie.save()

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

    

