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

    @staticmethod
    def post(request):
        serializer = CreativeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreatorDetail(APIView):
    @staticmethod
    def get(request, pk):
        creator = Creative.objects.get(pk=pk)
        serializer = CreativeSerializer(creator)
        return Response(serializer.data)