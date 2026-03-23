from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request,'home1.html',{'posts': posts})

# Create a post
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home1')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# Update a post
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home1')
    else:
        form = PostForm(instance=post)
    return render(request, 'update_post.html', {'form': form})

# Delete a post
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home1')
    return render(request, 'delete_post.html', {'post': post})


"""Django REST framework --- blog into REST APIs:"""

# GET → Fetch all posts
@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# POST → Create post
@api_view(['POST'])
def create_post_api(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# PUT → Update post 
@api_view(['PUT'])
def update_post_api(request, id):
    post = Post.objects.get(id=id)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# DELETE → Delete post
@api_view(['DELETE'])
def delete_post_api(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return Response({"message": "Post deleted"})