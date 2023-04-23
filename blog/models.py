from django.conf import settings

from django.db import models


class BlogUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar/blank-profile-picture.png')
    website = models.URLField(blank=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)


class Comment(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    is_reviewed = models.BooleanField(default=False)
