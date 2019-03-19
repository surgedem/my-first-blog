from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone


def home(request):
    return render(request, 'about.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'about.html')


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'about.html', {'posts': posts})


# Create your views here.
