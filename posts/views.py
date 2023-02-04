from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from base.models import WebUser

# Create your views here.
def uploadpost(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.method == 'POST':
        # print(request.POST['desc'])
        postuser = User.objects.get(username=request.user)
        postdesc = request.POST['desc']
        # if Post.objects.filter(author=postuser, post_body=postdesc):
        duplicate = len(Post.objects.filter(author=postuser, post_body=postdesc))
        posts = Post.objects.create(author=postuser, post_body=postdesc, duplicate_post=duplicate)
    return HttpResponseRedirect(reverse('index'))

def deletepost(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.method == 'POST':
        postuser = User.objects.get(username=request.user)
        postdesc = request.POST['desc']
        postdupe = request.POST['dupe']
        Post.delete(Post.objects.get(author=postuser, post_body=postdesc, duplicate_post=postdupe))
    return HttpResponseRedirect(reverse('index'))
