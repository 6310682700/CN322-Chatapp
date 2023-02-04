from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from base.models import WebUser

# Create your views here.
def uploadpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(username=request.user)
            postdesc = request.POST['desc']
            posts = Post.objects.create(author=request.user, post_body = postdesc)
        return render(request,'index.html')
    else:
        return HttpResponseRedirect(reverse('login'))