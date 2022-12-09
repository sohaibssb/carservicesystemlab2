from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Car
        fields = ['id', 'car_uid', 'brand' , 'model' , 'registration_number' , 'power' , 'price' , 'type' , 'availability']
