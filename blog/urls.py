from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='home'),
    path('create/', views.BlogPostCreateView.as_view(), name='create_post'),

]
