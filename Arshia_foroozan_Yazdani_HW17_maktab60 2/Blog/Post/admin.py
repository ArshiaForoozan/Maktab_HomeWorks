from django.contrib import admin
from .models import Post, comment, Tag

admin.site.register(Post)
admin.site.register(comment)
admin.site.register(Tag)