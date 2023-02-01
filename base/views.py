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