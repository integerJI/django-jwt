from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .models import Post

def posts(request):
    posts = Post.objects.filter(
        published_at__isnull=False).order_by('-published_at')
    return render(request, 'blog/posts.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def json_posts(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JWTAuthentication,))
def jwt_posts(request):
    posts = Post.objects.filter(
        published_at__isnull=False).order_by('-published_at')
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")
