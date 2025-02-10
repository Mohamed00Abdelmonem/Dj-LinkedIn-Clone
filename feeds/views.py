from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework import generics
from .models import Post

class PostListAPI(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    