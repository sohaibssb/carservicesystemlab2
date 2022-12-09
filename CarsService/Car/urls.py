from django.contrib import admin
from django.urls import path
from Car import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CarViewSet


urlpatterns=[
 
    path('cars',CarViewSet.as_view({
        'get':'Cars'
    })),
     path('cars/<str:pk>',CarViewSet.as_view({
        'get':'ACar'
    })),
]
