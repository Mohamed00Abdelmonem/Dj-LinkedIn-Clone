from django.urls import path
from .views import PostListAPI

urlpatterns = [
    path('', PostListAPI.as_view())
]
