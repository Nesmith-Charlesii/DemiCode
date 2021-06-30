from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Image, Bank, Blog, Digital_Product, Video, Review, Code_Snippet
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    # Write only stores password but doesn't include it in JSON
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'token')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'photo_upload', 'user', 'created_at', 'updated_at']


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'debit_card', 'user', 'created_at', 'updated_at']


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