from rest_framework import serializers
from .models import Rental

class RentalSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Rental
        fields = ['id', 'username', 'payment_uid' , 'car_uid' , 'date_from' , 'date_to' , 'status']

