from django.shortcuts import render
from .models import Image, Bank, Blog, Digital_Product, Review, Video, Code_Snippet
from .serializers import ImageSerializer, BankSerializer, BlogSerializer, Digital_ProductSerializer, ReviewSerializer, VideoSerializer, Code_SnippetSerializer, UserSerializer, UserSerializerWithToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
import bcrypt


@api_view(['GET'])
def current_user(request):
    # Determine current user by their token.
    serializer = UserSerializer(request.user)
    print(serializer)
    return Response(serializer.data)


# REGISTER USER
class UserList(APIView):

    permission_classes = [permissions.AllowAny]

    @staticmethod
    def post(request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            print(data['first_name'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogList(APIView):

    def post(self, request):
        userSerializer = UserSerializer(request.user)
        user = userSerializer.data
        print(f'Blog User Id', user['id'])
        # To attach User Id to Blog model as FK, userID must be from an instance of the User class
        userId = User.objects.get(id=user['id'])
        blogSerializer = BlogSerializer(data=request.data)
        if blogSerializer.is_valid():
            # Attach user's id to FK of new blog that is about to be created
            blogSerializer.validated_data['creator'] = userId
            blogSerializer.save()
            return Response(blogSerializer.data, status=status.HTTP_201_CREATED)
        return Response(blogSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogList2(APIView):
    def get(self, request):
        userSerializer = UserSerializer(request.user)
        user = userSerializer.data
        print(f'Blog Detail User Id', user['id'])
        blogs = Blog.objects.filter(creator_id=user['id'])
        blogSerializer = BlogSerializer(blogs, many=True)
        return Response(blogSerializer.data, status=status.HTTP_200_OK)


class BlogDetail(APIView):
    def put(self, request, pk):
        userSerializer = UserSerializer(request.user)
        user = userSerializer.data
        userId = User.objects.get(id=user['id'])
        blogSerializer = BlogSerializer(data=request.data)
        if blogSerializer.is_valid():
            blogSerializer.validated_data['creator'] = userId
            blogSerializer.save()
            return Response(blogSerializer.data, status=status.HTTP_200_OK)
        return Response(blogSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_200_OK)


class Digital_ProductList(APIView):

    def post(request):
        serializer = Digital_ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(request):
        products = Digital_Product.objects.all()
        serializer = Digital_ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Digital_ProductDetail(APIView):

    def get(request, pk):
        product = Digital_Product.objects.get(pk=pk)
        serializer = Digital_ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(request, pk):
        product = Digital_Product.objects.get(pk=pk)
        serializer = Digital_ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(request, pk):
        product = Digital_Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_200_OK)


class ReviewList(APIView):

    def post(request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewDetail(APIView):

    def get(self, request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(status=status.HTTP_200_OK)


class Code_SnippetList(APIView):

    def post(request):
        serializer = Code_SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(request):
        snippets = Code_Snippet.objects.all()
        serializer = Code_SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Code_SnippetDetail(APIView):

    def get(request, pk):
        snippet = Code_Snippet.objects.get(pk=pk)
        serializer = Code_SnippetSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(request, pk):
        snippet = Code_Snippet.objects.get(pk=pk)
        serializer = Code_SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(request, pk):
        snippet = Code_Snippet.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_200_OK)


class VideoList(APIView):

    def post(request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VideoDetail(APIView):

    def get(request, pk):
        video = Video.objects.get(pk=pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(request, pk):
        video = Video.objects.get(pk=pk)
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(request, pk):
        video = Video.objects.get(pk=pk)
        video.delete()
        return Response(status=status.HTTP_200_OK)


class LoginList(APIView):

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
