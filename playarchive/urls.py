from django.urls import path
from .views import ArchiveCreateView, ArchiveViewSet,ArchiveByTitleAPI,ArchiveEditAPIView,ArchiveDeleteAPIView,MovieCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('archive/', ArchiveViewSet.as_view(), name='archive-viewset'),
    path('archive/<str:title>/',ArchiveByTitleAPI.as_view(), name='archive-by-title'),
    path('create-archive/', ArchiveCreateView.as_view(), name='archive-create'),
    path('edit-archive/<str:title>/', ArchiveEditAPIView.as_view(), name='archive-edit-api'),
    path('delete/<str:title>/',ArchiveDeleteAPIView.as_view(), name='archive-delete-api'),
    path('create-movie/', MovieCreateView.as_view(), name='create_movie'),
]
