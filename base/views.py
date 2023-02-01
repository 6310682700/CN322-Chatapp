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
    if request.user.is_authenticated:
<<<<<<< HEAD
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')

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

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
=======
        return render(request, 'index')
    else:
        return HttpResponseRedirect(reverse('login'))

def login_view(request):
    # if request.method == "GET":
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return HttpResponseRedirect(reverse('index'))
        # else:
        #     return render(request, 'index')

        return render(request, 'login.html')
>>>>>>> 7a124f7f399b74a43aaf91b1c8f9d76b65e12f91
