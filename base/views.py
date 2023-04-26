from audioop import reverse
from cgitb import html
from email import message
from http.client import HTTPResponse
from re import sub
import re
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from posts.models import Post

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        # post = Post.objects.filter(author=user)
        post = Post.objects.all()
        print(post)
        return render(request, 'index.html', {
            'user': user,
            'posts': post,
        })
    else:
        return HttpResponseRedirect(reverse('login'))

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
