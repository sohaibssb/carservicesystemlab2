from django.http import JsonResponse
from .models import CarsService
from .serializers import CarSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

@api_view(['GET'])
def car_list(request, format=None):
        cars = CarsService.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

 
