from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import Post_form


#### post view
@require_GET
def post_list(request):
    posts = Post.objects.all().order_by("-id")
    context = {"posts" : posts}
    return render(request, "post/post_list.html", context)


@require_GET
def post_detail(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    context = {"post" : post}
    return render(request, "post/post_detail.html", context)


#### CRUD
@require_http_methods(["GET", "POST"])
@login_required
def post_create(request):
    if request.method == 'GET':
        form = Post_form
        context = {
            "form" : form,
            "crud" : 1,
            }
        return render(request, "post/post_form.html", context)
        
    if request.method == 'POST':
        form = Post_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
        return redirect("post:post_list")


@require_http_methods(["GET", "POST"])
@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'GET':
        form = Post_form(instance=post)
        context = {
            'form' : form,
            'post' : post,
            'crud' : 2,
        }
        return render(request, "post/post_form.html", context)
        
    if request.method == 'POST':
        form = Post_form(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
        return redirect("post:post_detail", post.id)


@require_http_methods(["GET", "POST"])
@login_required
def post_delete(request, id):
    if request.method == 'GET':
        post = get_object_or_404(Post, id=id)
        return redirect("post:post_detail", post.id)
        
    if request.method == 'POST':
        post = get_object_or_404(Post, id=id)
        post.delete()
        return redirect("post:post_list")