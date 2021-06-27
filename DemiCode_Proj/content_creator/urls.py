from django.urls import path
from . import views

urlpatterns = [
    path('content_creators/', views.CreatorList.as_view()),
    path('content_creator/<int:pk>/', views.CreatorDetail.as_view()),
    path('blog_content/', views.BlogList.as_view()),
    path('blog_content/<int:pk>/', views.BlogDetail.as_view()),
    path('digital_products/', views.Digital_ProductList.as_view()),
    path('digital_product/<int:pk>/', views.Digital_ProductDetail.as_view())
]
