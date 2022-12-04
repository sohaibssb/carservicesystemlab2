from rest_framework import serializers
from .models import CarsService

class CarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CarsService
        fields = ['id', 'car_uid', 'brand' , 'model' , 'registration_number' , 'power' , 'price' , 'type' , 'availability']
