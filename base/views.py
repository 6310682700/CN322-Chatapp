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
from cryptography.fernet import Fernet, InvalidToken



from posts.models import Post

# Create your views here.

key = b'1K_zeuLoLakuMS3ih38_6INKX7BPIKJDLLHT3XrG4yo='
cipher_suite = Fernet(key)

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        post = Post.objects.all()
        decrypted_posts = []

        for p in post:
            try:
                decrypted_desc = cipher_suite.decrypt(p.post_body).decode()  # Decrypt the post description
            except InvalidToken:
                decrypted_desc = "Error decrypting post"

            decrypted_posts.append({
                'id': p.id,
                'author': p.author,
                'post_body': decrypted_desc,
                'created_at':p.created_at,
                'updated_at': p.updated_at,
                'duplicate_post': p.duplicate_post
            })

        return render(request, 'index.html', {
            'user': user,
            'posts': decrypted_posts,
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
