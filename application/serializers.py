from rest_framework import serializers
from .models import Video, News


class VideoCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class NewsCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
