from typing import Callable
from django.db import models
from django.db.models.fields import CharField, DateField, SlugField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from slugify import slugify


class Post(models.Model):
    title = CharField(max_length=30)
    slug = SlugField(unique=True, null=True, blank=True)
    description = TextField()
    created_at = DateField(auto_now_add=True)
    author = CharField(max_length=30)
    tag = ManyToManyField('Tag', null=True, blank=True)
    image = ImageField(upload_to='uploads', null=True, blank=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class comment(models.Model):
    post = ForeignKey('Post', null=True, on_delete=models.CASCADE)
    text = CharField(max_length=255)
    updated_at = DateField(auto_now=True)
    def __str__(self):
        return self.text[:10]

class Tag(models.Model):
    tag_title = models.CharField(max_length=255)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tag_title