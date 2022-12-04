from django.contrib import admin
from django.urls import path
from RentalService import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
   
     path('rental',views.user_list, name='user_list'),
     path('rental/<int:id>',views.UserInf,name='UserInf')
    
]

urlpatterns = format_suffix_patterns(urlpatterns)

