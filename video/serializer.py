from rest_framework import serializers
from .models import video

# serializer class for defining the resposnse format of API
class VideoViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields = ['id', 'title', 'description', 'thumbnail','publishedAt','tags']