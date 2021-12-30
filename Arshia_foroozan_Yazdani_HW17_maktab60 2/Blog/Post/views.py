from django.shortcuts import render
from rest_framework import generics
from .models import Post, comment
from .serializers import PostSerializer, CommentSerializer

class PostApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentApiView(generics.ListAPIView):
    queryset = comment.objects.all()
    serializer_class = CommentSerializer

class CommentApiVDetail(generics.RetrieveAPIView):
    queryset = comment.objects.all()
    serializer_class = CommentSerializer

class PostApiDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer