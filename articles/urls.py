from django.urls import path
from .views import ArticleListCreateView

urlpatterns = [
    path('create/', ArticleListCreateView.as_view(), name='article-list-create'),
]
