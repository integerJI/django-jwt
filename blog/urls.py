from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('json_posts/', views.json_posts, name='json_posts'),
]
