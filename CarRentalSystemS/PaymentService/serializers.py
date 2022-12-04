from rest_framework import serializers
from .models import PaymentService

class PaymentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PaymentService
        fields = ['id', 'payment_uid' , 'status' , 'price' ]

  
   