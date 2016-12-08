from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.


def logout_top(request):
    return render(request, 'shougisite/logout_top.html', {})
