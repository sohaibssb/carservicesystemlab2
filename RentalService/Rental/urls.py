from django.contrib import admin
from django.urls import path
from Rental import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RentalViewSet


urlpatterns=[
    path('rentals',RentalViewSet.as_view({
        'get':'Rentals',
        'post':'createRental'
    })),
    path('rentals/<str:rental_uid>',RentalViewSet.as_view({
        'get':'GetRental',
        'patch':'cancelRental'
    })),
]