from rest_framework import serializers
from .models import Creative, Blog, Digital_Product, Video, Review, Code_Snippet


class CreativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creative
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'confirmPW', 'debit_card', 'photo_upload', 'created_at', 'updated_at']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'header_image', 'creator', 'created_at', 'updated_at']


class Digital_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digital_Product
        fields = ['id', 'name', 'description', 'image', 'price', 'seller', 'created_at', 'updated_at']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video', 'creator', 'created_at', 'updated_at']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'comment', 'anon_name', 'Thumbs_Upped', 'Likes', 'creator', 'blog', 'created_at', 'updated_at']


class Code_SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code_Snippet
        fields = ['id', 'title', 'text', 'upload', 'creator', 'created_at', 'updated_at']