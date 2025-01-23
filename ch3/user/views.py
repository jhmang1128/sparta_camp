from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import User
from .forms import UserChangeForm_custom, UserCreationForm_custom


#### user
@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
            
    else:
        form = AuthenticationForm()
        context = {"form" : form}
        return render(request, "user/login.html", context)


@require_POST
@login_required
def logout(request):
    auth_logout(request)
    return redirect('index')


#### user CRUD
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = UserCreationForm_custom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        
    else:
        form = UserCreationForm_custom()
        context = {"form": form}
        return render(request, "user/signup.html", context)


@require_POST
@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('index')


@require_http_methods(["GET", "POST"])
def profile(request):
    if request.method == "POST":
        form = UserChangeForm_custom(request.POST, instance=request.user) # 업데이트 폼 변경
        if form.is_valid():
            form.save()
            return redirect("index")
        
    else:
        form = UserChangeForm_custom(instance=request.user)
        context = {"form": form}
        return render(request, "user/profile.html", context)