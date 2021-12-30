from django.http import response
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post, comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import APIView

class PostApiView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentApiView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = comment.objects.all()
    serializer_class = CommentSerializer

class CommentApiVDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = comment.objects.all()
    serializer_class = CommentSerializer

class PostApiDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentPostApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, pk):
        comments = comment.objects.filter(post__id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)