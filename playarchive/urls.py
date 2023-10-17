from django.urls import path
from .views import ArchiveCreateView, ArchiveViewSet,ArchiveByTitleAPI

urlpatterns = [
    path('archive/', ArchiveViewSet.as_view(), name='archive-viewset'),
    path('archive/<str:title>/',ArchiveByTitleAPI.as_view(), name='archive-by-title'),
    path('create-archive/', ArchiveCreateView.as_view(), name='archive-create'),
]
