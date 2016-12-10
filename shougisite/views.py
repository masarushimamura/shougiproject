from django.shortcuts import render
from django.utils import timezone
from . import forms

# Create your views here.


def logout_top(request):
    return render(request, 'shougisite/logout_top.html', {})


def login_top(request):
    form = forms.login_Form(request.GET or None)
    if form.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'
    d = {
        'form': form,
        'message': message,
    }
    return render(request, 'shougisite/login_top.html', d)


def mypage_top(request):
    return render(request, 'shougisite/mypage_top.html', {})


def mypage_add(request):
    return render(request, 'shougisite/mypage_add.html', {})