from django.contrib.auth.models import User

from django.db import models


class BlogUser(models.Model):
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/')
    website = models.URLField()


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    text = models.TextField()
    image = models.ImageField(upload_to='posts/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_draft = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)


class Comment(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    is_reviewed = models.BooleanField(default=False)
