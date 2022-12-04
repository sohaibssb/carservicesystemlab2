from django.contrib import admin
from django.urls import path
from CarsService import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
     path('cars',views.car_list, name='car_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)




