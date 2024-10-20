"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
from . import views
from .views import post, post_list, post_create, post_detail  

urlpatterns = [
    path("", include("api.urls")),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('',post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
]

