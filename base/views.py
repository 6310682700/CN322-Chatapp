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
