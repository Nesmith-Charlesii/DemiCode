from .models import Image, Bank, Blog, Digital_Product, Review, Video, Code_Snippet
from .serializers import ImageSerializer, BlogSerializer, Digital_ProductSerializer, ReviewSerializer, VideoSerializer, Code_SnippetSerializer, UserSerializer, UserSerializerWithToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from django.conf import settings
import stripe
# "SECRET" test key from stripe quickstart link
stripe.api_key = "sk_test_51J8TYoEbNvMl2Uk9yxkCLEMt2qARtRueHGEwR1ui5LkPFkKWAs6ffs6QoKfzl7lMyGWawv5eYrNatM6EJ4hIRDMF00OzJYf54p"


@api_view(['GET'])
def current_user(request):
    # Determine current user by their token.
    serializer = UserSerializer(request.user)
    # print('CURRENT USER', serializer)
    return Response(serializer.data)


class UserList(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            # print(data['first_name'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogList(APIView):

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        userSerializer = UserSerializer(request.user)
        user = userSerializer.data
        # print(f'Blog User Id', user['id'])
        # To attach User Id to Blog model as FK, userID must be from an instance of the User class
        userId = User.objects.get(id=user['id'])
        print(userId.first_name)
        blogSerializer = BlogSerializer(data=request.data)
        print('Blog Serializer', blogSerializer)
        if blogSerializer.is_valid():
            # Attach user's id to FK of new blog that is about to be created
            blogSerializer.validated_data['creator'] = userId
            blogSerializer.save()
            return Response(blogSerializer.data, status=status.HTTP_201_CREATED)
        return Response(blogSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        userSerializer = UserSerializer(request.user)
        user = userSerializer.data
        # print(f'Blog Detail User Id', user['id'])
        blogs = Blog.objects.filter(creator_id=user['id'])
        blogSerializer = BlogSerializer(blogs, many=True)
        return Response(blogSerializer.data, status=status.HTTP_200_OK)


class BlogList2(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        userSerializer = UserSerializer(request.user)
        user = userSerializer.data
        # print(f'Blog User Id', user['id'])
        userId = User.objects.get(id=user['id'])
        productSerializer = Digital_ProductSerializer(data=request.data)
        if productSerializer.is_valid():
            productSerializer.validated_data['seller'] = userId
            productSerializer.save()
            return Response(productSerializer.data, status=status.HTTP_201_CREATED)
        return Response(productSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        userSerializer = UserSerializer(request.user)
        user = userSerializer.data
        products = Digital_Product.objects.filter(seller_id=user['id'])
        productSerializer = Digital_ProductSerializer(products, many=True)
        return Response(productSerializer.data, status=status.HTTP_200_OK)


class Digital_ProductList2(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        products = Digital_Product.objects.all()
        serializer = Digital_ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Digital_ProductDetail(APIView):

    # def get(request, pk):
    #     product = Digital_Product.objects.get(pk=pk)
    #     serializer = Digital_ProductSerializer(product)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = Digital_Product.objects.get(pk=pk)
        serializer = Digital_ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = Digital_Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_200_OK)


class ReviewList(APIView):

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
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

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        userSerializer = UserSerializer(request.user)
        user = userSerializer.data
        userId = User.objects.get(id=user['id'])
        # print(request.data)
        snippetSerializer = Code_SnippetSerializer(data=request.data)
        print(snippetSerializer)
        if snippetSerializer.is_valid():
            snippetSerializer.validated_data['creator'] = userId
            print('Validated Snippet', snippetSerializer.validated_data)
            snippetSerializer.save()
            return Response(snippetSerializer.data, status=status.HTTP_201_CREATED)
        return Response(snippetSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        userSerializer = UserSerializer(request.user)
        user = userSerializer.data
        snippets = Code_Snippet.objects.filter(creator_id=user['id'])
        snippetSerializer = Code_SnippetSerializer(snippets, many=True)
        return Response(snippetSerializer.data, status=status.HTTP_200_OK)


class Code_SnippetList2(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        snippets = Code_Snippet.objects.all()
        serializer = Code_SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Code_SnippetDetail(APIView):

    def get(self, request, pk):
        snippet = Code_Snippet.objects.get(pk=pk)
        serializer = Code_SnippetSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        snippet = Code_Snippet.objects.get(pk=pk)
        serializer = Code_SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = Code_Snippet.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_200_OK)


class VideoList(APIView):

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        userSerializer = UserSerializer(request.user)
        user = userSerializer.data
        userId = User.objects.get(id=user['id'])
        videoSerializer = VideoSerializer(data=request.data)
        if videoSerializer.is_valid():
            videoSerializer.validated_data['creator'] = userId
            videoSerializer.save()
            return Response(videoSerializer.data, status=status.HTTP_201_CREATED)
        return Response(videoSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        userSerializer = UserSerializer(request.user)
        user = userSerializer.data
        videos = Video.objects.filter(creator_id=user['id'])
        videoSerializer = VideoSerializer(videos, many=True)
        return Response(videoSerializer.data, status=status.HTTP_200_OK)


class VideoList2(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        videos = Video.objects.all()
        for video in videos:
            print(video.video)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VideoDetail(APIView):

    def get(self, request, pk):
        video = Video.objects.get(pk=pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        video = Video.objects.get(pk=pk)
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        video = Video.objects.get(pk=pk)
        video.delete()
        return Response(status=status.HTTP_200_OK)


class PaymentList(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        test_payment_intent = stripe.PaymentIntent.create(
            amount=1000,
            currency='usd',
            payment_method_types=['card'],
            receipt_email='nesmith.charlesii@gmail.com')
        return Response(status=status.HTTP_200_OK, data=test_payment_intent)


class Save_Stripe_Info(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        email = data['email']
        payment_method_id = data['payment_method_id']
        extra_msg = ''

        # check if customer with provided email already exists
        customer_data = stripe.Customer.list(email=email).data

        # if array is empty, the email has not been used yet
        if len(customer_data) == 0:
            # creating customer
            customer = stripe.Customer.create(email=email, payment_method=payment_method_id)
        else:
            customer = customer_data[0]
            extra_msg = "Customer already exists"

        stripe.PaymentIntent.create(
            customer=customer,
            payment_method=payment_method_id,
            currency='usd',
            amount=2000,
            confirm=True
        )

        return Response(data={'message': 'Success', 'data': {'customer_id': customer.id, 'extra_msg': extra_msg}}, status=status.HTTP_200_OK)


class ImageList(APIView):

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        userSerializer = UserSerializer(request.user)
        user = userSerializer.data
        userId = User.objects.get(id=user['id'])
        # current_image = Image.objects.filter(user_id=userId).filter().only('id').delete()

        # print(request.data)
        imageSerializer = ImageSerializer(data=request.data)
        print(imageSerializer)
        if imageSerializer.is_valid():
            imageSerializer.validated_data['user'] = userId
            imageSerializer.save()
            return Response(imageSerializer.data, status=status.HTTP_201_CREATED)
        return Response(imageSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        userSerializer = UserSerializer(request.user)
        user = userSerializer.data
        image = Image.objects.filter(user_id=user['id']).first()
        print(image)
        if image is None:
            media_url = settings.MEDIA_URL
            path_to_user_folder = media_url + "images/user.png"
            print(path_to_user_folder)
            return Response(path_to_user_folder, status=status.HTTP_200_OK)
        imageSerializer = ImageSerializer(image)
        return Response(imageSerializer.data, status=status.HTTP_200_OK)




