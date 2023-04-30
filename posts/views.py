from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from cryptography.fernet import Fernet


from .models import Post
from base.models import WebUser

# Use your securely stored key here
key = b'1K_zeuLoLakuMS3ih38_6INKX7BPIKJDLLHT3XrG4yo='
cipher_suite = Fernet(key)

# Create your views here.
def uploadpost(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.method == 'POST':
        postuser = User.objects.get(username=request.user)
        postdesc = request.POST['desc']
        encrypted_desc = cipher_suite.encrypt(postdesc.encode()).decode()  # Encrypt the post description
        duplicate = len(Post.objects.filter(author=postuser, post_body=encrypted_desc))
        posts = Post.objects.create(author=postuser, post_body=encrypted_desc, duplicate_post=duplicate)
    return HttpResponseRedirect(reverse('index'))

def deletepost(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.method == 'POST':
        postuser = User.objects.get(username=request.user)
        postdesc = request.POST['desc']
        encrypted_desc = cipher_suite.encrypt(postdesc.encode())  # Encrypt the post description
        postdupe = request.POST['dupe']
        Post.delete(Post.objects.get(author=postuser, post_body=encrypted_desc, duplicate_post=postdupe))
    return HttpResponseRedirect(reverse('index'))