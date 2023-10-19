from django.urls import path
from .views import ArticleListCreateView,ArticleViewSet,CategoryViewSet,TagViewSet

urlpatterns = [
    path('create/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('list/', ArticleViewSet.as_view(), name='list'),
    path('category/', CategoryViewSet.as_view(), name='category'),
    path('tag/', TagViewSet.as_view(), name='tag')
]
