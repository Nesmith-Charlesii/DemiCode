from django.urls import path
from . import views

urlpatterns = [
    path('content_creators/', views.CreatorList.as_view()),
]
