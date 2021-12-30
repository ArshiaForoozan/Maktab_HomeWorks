from django.db.models import fields
from rest_framework import serializers
from .models import Post, comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'author', 'description', 'created_at')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'


