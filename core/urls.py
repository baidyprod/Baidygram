from blog.views import BlogPostCreateView, BlogPostDetailView, BlogPostListView, BlogPostUpdateView, \
    CommentCreateView, RegisterFormView, UpdateProfile, UserProfile, contact_us

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', BlogPostListView.as_view(), name='home'),

    path('create_post/', BlogPostCreateView.as_view(), name='create_post'),
    path("contact/", contact_us, name="contact_us"),

    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/register/", RegisterFormView.as_view(), name="register"),
    path("accounts/update_profile/", UpdateProfile.as_view(), name="update_profile"),

    path("profile/<str:username>/", UserProfile.as_view(), name="profile"),
    path("profile/<str:username>/<int:pk>/", BlogPostDetailView.as_view(), name="blogpost_detail"),
    path("profile/<str:username>/<int:pk>/update/", BlogPostUpdateView.as_view(), name="blogpost_update"),
    path("profile/<str:username>/<int:pk>/comment/", CommentCreateView.as_view(), name="comment_create"),

]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
