"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from blog.views import RegisterFormView, UpdateProfile, UserProfile, BlogPostDetailView, BlogPostUpdateView, \
    CommentCreateView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include('blog.urls')),

    path("", include('django.contrib.auth.urls')),
    path("register/", RegisterFormView.as_view(), name="register"),
    path("update_profile/", UpdateProfile.as_view(), name="update_profile"),

    path("<str:username>/", UserProfile.as_view(), name="profile"),
    path("<str:username>/<int:pk>/", BlogPostDetailView.as_view(), name="blogpost_detail"),
    path("<str:username>/<int:pk>/update/", BlogPostUpdateView.as_view(), name="blogpost_update"),
    path("<str:username>/<int:pk>/comment/", CommentCreateView.as_view(), name="comment_create"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]