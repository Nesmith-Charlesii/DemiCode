from django.shortcuts import render
from .models import Creative, Blog, Digital_Product, Review, Video, Code_Snippet
from .serializers import CreativeSerializer, BlogSerializer, Digital_ProductSerializer, ReviewSerializer, VideoSerializer, Code_SnippetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
