from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'chat_base.html')
    else:
        return HttpResponseRedirect(reverse('login'))

def room(request, room_name):
    if request.user.is_authenticated:
        return render(request, 'chatroom.html', {
            'room_name' : room_name
        })
    else:
        return HttpResponseRedirect(reverse('login'))