from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


# Create your views here.
