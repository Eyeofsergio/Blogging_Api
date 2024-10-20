from rest_framework import serializers
from .models import BloggingPost

#Create Class And Links

class BloggingPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloggingPost
        fields = ['id', 'title', 'content','published_date']
        