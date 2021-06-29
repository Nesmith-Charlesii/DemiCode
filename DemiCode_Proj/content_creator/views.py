from django.shortcuts import render
from .models import Creative, Blog, Digital_Product, Review, Video, Code_Snippet
from .serializers import CreativeSerializer, BlogSerializer, Digital_ProductSerializer, ReviewSerializer, VideoSerializer, Code_SnippetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
import bcrypt


# Create your views here.
class CreatorList(APIView):
    @staticmethod
    def get(request):
        creators = Creative.objects.all()
        serializer = CreativeSerializer(creators, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        hashed_Password = bcrypt.hashpw(request.data["password"].encode(), bcrypt.gensalt()).decode()
        request.data["password"] = hashed_Password
        serializer = CreativeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.validated_data["password"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreatorDetail(APIView):
    @staticmethod
    def get(request, pk):
        creator = Creative.objects.get(pk=pk)
        serializer = CreativeSerializer(creator)
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        creator = Creative.objects.get(pk=pk)
        serializer = CreativeSerializer(creator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        creator = Creative.objects.get(pk=pk)
        creator.delete()
        return Response(status=status.HTTP_200_OK)


class BlogList(APIView):
    @staticmethod
    def post(request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogDetail(APIView):
    @staticmethod
    def get(request, pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request, pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_200_OK)


class Digital_ProductList(APIView):
    @staticmethod
    def post(request):
        serializer = Digital_ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        products = Digital_Product.objects.all()
        serializer = Digital_ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Digital_ProductDetail(APIView):
    @staticmethod
    def get(request, pk):
        product = Digital_Product.objects.get(pk=pk)
        serializer = Digital_ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request, pk):
        product = Digital_Product.objects.get(pk=pk)
        serializer = Digital_ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        product = Digital_Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_200_OK)


class ReviewList(APIView):
    @staticmethod
    def post(request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewDetail(APIView):
    @staticmethod
    def get(request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(status=status.HTTP_200_OK)


class Code_SnippetList(APIView):
    @staticmethod
    def post(request):
        serializer = Code_SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        snippets = Code_Snippet.objects.all()
        serializer = Code_SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Code_SnippetDetail(APIView):
    @staticmethod
    def get(request, pk):
        snippet = Code_Snippet.objects.get(pk=pk)
        serializer = Code_SnippetSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request, pk):
        snippet = Code_Snippet.objects.get(pk=pk)
        serializer = Code_SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        snippet = Code_Snippet.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_200_OK)


class VideoList(APIView):
    @staticmethod
    def post(request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VideoDetail(APIView):
    @staticmethod
    def get(request, pk):
        video = Video.objects.get(pk=pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request, pk):
        video = Video.objects.get(pk=pk)
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        video = Video.objects.get(pk=pk)
        video.delete()
        return Response(status=status.HTTP_200_OK)


class LoginList(APIView):
    @staticmethod
    def post(request):
        print(request.data)
        # Use .get to access a single object's properties. .filter will return a queryset
        user = Creative.objects.get(username=request.data["username"])
        print('USER', user.username)
        if bcrypt.checkpw(request.data['password'].encode(), user.password.encode()):
            print(True)
        else:
            print(False)
        return Response(request.data)