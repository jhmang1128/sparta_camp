from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import Post_form


def post_list(request):
    posts = Post.objects.all().order_by("-id")
    context = {"posts" : posts}
    return render(request, "post/post_list.html", context)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {"post" : post}
    return render(request, "post/post_detail.html", context)

def post_create(request):
    if request.method == 'GET':
        form = Post_form
        context = {"form" : form}
        return render(request, "post/post_create.html", context)
        
    if request.method == 'POST':
        form = Post_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect("post:post_list")
    
    
def post_update(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'GET':
        form = Post_form(instance=post)
        context = {
            'form' : form,
            'post' : post,
        }
        return render(request, "post/post_form.html", context)
        
    if request.method == 'POST':
        form = Post_form(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
        return redirect("post:post_detail", post.id)


def post_delete(request, id):
    if request.method == 'GET':
        return redirect("post:post_detail", post.id)
        
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.delete()
        return redirect("post:post_list")