from django.shortcuts import render

# Create your views here.

from .models import Post

def home(request):
    return render(request, 'trangchu.html')