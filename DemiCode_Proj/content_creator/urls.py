from django.urls import path
from . import views

urlpatterns = [
    path('content_creators/', views.CreatorList.as_view()),
    path('content_creator/<int:pk>/', views.CreatorDetail.as_view()),
    path('blog_content/', views.BlogList.as_view()),
    path('blog_content/<int:pk>/', views.BlogDetail.as_view()),
    path('digital_products/', views.Digital_ProductList.as_view()),
    path('digital_product/<int:pk>/', views.Digital_ProductDetail.as_view()),
    path('reviews/', views.ReviewList.as_view()),
    path('review/<int:pk>/', views.ReviewDetail.as_view()),
    path('code_snippets/', views.Code_SnippetList.as_view()),
    path('code_snippet/<int:pk>/', views.Code_SnippetDetail.as_view()),
    path('videos/', views.VideoList.as_view()),
    path('video/<int:pk>/', views.VideoDetail.as_view())
]
