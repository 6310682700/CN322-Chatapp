from audioop import reverse
from cgitb import html
from email import message
from http.client import HTTPResponse
from re import sub
import re
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('admin:index'))
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))