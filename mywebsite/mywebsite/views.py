from django.shortcuts import render
from django.http import HttpResponse
from .models import Post  

def home(request):
    return render(request, 'home.html')

# POst models/views

def post_list(request):
    posts = Post.objects.all() 
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)  
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
       
        return HttpResponse("Post created!")  
    return render(request, 'blog/post_create.html')  