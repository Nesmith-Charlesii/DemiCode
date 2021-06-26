from django.shortcuts import render
from .models import Creative, Blog, Digital_Product, Review, Video, Code_Snippet
from .serializers import CreativeSerializer, BlogSerializer, Digital_ProductSerializer, ReviewSerializer, VideoSerializer, Code_SnippetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CreatorList(APIView):
    @staticmethod
    def get(request):
        creator = Creative.objects.all()
        serializer = CreativeSerializer(creator, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)