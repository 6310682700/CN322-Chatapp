from django.shortcuts import render
from base.models import WebUser

from .models import Post

# Create your views here.
def uploadpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = WebUser.objects.get(username=request.user)
            postdesc = request.POST['desc']
            posts = Post.objects.create(author=request.user, post_body = postdesc)
        return render(request,'index.html')
    else:
        return redirect("login")