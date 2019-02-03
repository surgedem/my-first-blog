from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('about', include('blog.urls')),
    path('blog', include('blog.urls')),
]
