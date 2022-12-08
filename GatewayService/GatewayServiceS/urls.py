
from django.urls import path
from django.contrib import admin
from .views import GatewayViewSet

urlpatterns=[
    path('rentals',GatewayViewSet.as_view({
        'get':'UserRentals',
        'post':'BookCar'
    })),
     path('rentals/<str:rental_uid>',GatewayViewSet.as_view({
        'get':'UserSpecificRental',
        'delete':'cancelRental'
    })),
    path('cars',GatewayViewSet.as_view({
        'get':'cars'
    })),

]