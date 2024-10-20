# Connect the views and the urls 

from django.urls import path
from .views import post_list, post_detail, post_create, views

urlpatters = [
    path('BloggingPost/', views.BloggingPostListCreate.as_view(), name='blogpost-view-create'),
    path('BloggerPost/int:pk/', views.BloggerPostRetrieveUpdateDestroy.as_view(),name='update'),
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
]