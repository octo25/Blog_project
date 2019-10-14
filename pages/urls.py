from django.urls import path
from .views import HomePageView, GalleryPageView

urlpatterns = [
   path('', HomePageView.as_view(), name='home'),
   path('gallery/', GalleryPageView.as_view(), name='gallery'),
]