from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='blog-about'),
    path('post/', views.post_list, name='post-list'),
]
