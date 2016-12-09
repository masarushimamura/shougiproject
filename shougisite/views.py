from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.


def logout_top(request):
    return render(request, 'shougisite/logout_top.html', {})


def login_top(request):
    return render(request, 'shougisite/login_top.html', {})


def mypage_top(request):
    return render(request, 'shougisite/mypage_top.html', {})


def mypage_add(request):
    return render(request, 'shougisite/mypage_add.html', {})