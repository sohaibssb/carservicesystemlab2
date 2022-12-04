from rest_framework import serializers
from .models import RentalService

class RentalSerializer(serializers.ModelSerializer):
    class Meta: 
        model = RentalService
        fields = ['id', 'username', 'payment_uid' , 'car_uid' , 'date_from' , 'date_to' , 'status']

