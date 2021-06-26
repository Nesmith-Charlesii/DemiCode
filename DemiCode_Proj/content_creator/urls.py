from django.urls import path
from . import views

urlpatterns = [
    path('content_creators/', views.CreatorList.as_view()),
    path('content_creator/<int:pk>/', views.CreatorDetail.as_view()),
    # path('blog_content/', views.BlogList.as_view())
]
