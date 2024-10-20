# Import a generic view to then customize to your liking.

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BloggingPost
from .serializers import BloggingPostSerializer 
from rest_framework.views import APIView

# Create your views here.

class BloggingPostListCreate(generics.ListCreateAPIView):
    queryset = BloggingPost.objects.all()
    serializer_class = BloggingPostSerializer

    def delete(self,request, *args, **kwargs):
        BloggingPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BloggerPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloggingPost.objects.all()
    serializer_class = BloggingPostSerializer
    Lookup_field = 'pk'

    #24 mins continue from there