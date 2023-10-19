from rest_framework import views, status
from rest_framework.response import Response
from .models import Article,Category,Tag
from django.contrib.auth.models import User
from .serializers import ArticleSerializer,CategorySerializer,TagSerializer

class ArticleListCreateView(views.APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        
        print(serializer)

        if serializer.is_valid():
            # Adminユーザーを取得
            admin_user = User.objects.get(username='Admin')

            # authorをAdminユーザーに設定
            serializer.validated_data['author'] = admin_user

            # categoryの名前を元にオブジェクトを取得し、それをvalidated_dataに設定
            category_name = request.data.get('category')
            if category_name:
                try:
                    category = Category.objects.get(name=category_name)
                    serializer.validated_data['category'] = category
                except Category.DoesNotExist:
                    return Response({"error": "Category not found"}, status=status.HTTP_400_BAD_REQUEST)
                
            tag_name = request.data.get('tags')
            print(tag_name)
            if tag_name:
                try:
                    tag = Tag.objects.get(name=tag_name)
                    serializer.validated_data['tags'] = [tag]  # タグのリストとして設定
                except Tag.DoesNotExist:
                    return Response({"error": f"Tag '{tag_name}' not found"}, status=status.HTTP_400_BAD_REQUEST)


                
                
            

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ArticleViewSet(views.APIView):
    def get_queryset(self):
        return Article.objects.all()
    
    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        
        serializer = ArticleSerializer(posts, many=True)
        return Response(serializer.data)
    
class CategoryViewSet(views.APIView):
    def get_queryset(self):
        return Category.objects.all()
    
    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        
        serializer = CategorySerializer(posts, many=True)
        return Response(serializer.data)
    
class TagViewSet(views.APIView):
    def get_queryset(self):
        return Tag.objects.all()
    
    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        
        serializer = TagSerializer(posts, many=True)
        return Response(serializer.data)