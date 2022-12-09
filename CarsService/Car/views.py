from django.http import JsonResponse
from .models import Car
from .serializers import CarSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from pytz import timezone

 
class CarViewSet(viewsets.ViewSet):
    def __init__(self):
        if Car.objects.count()==0:
            car=Car(car_uid="109b42f3-198d-4c89-9276-a7520a7120ab",brand="Mercedes Benz",model="GLA 250", registration_number = "ЛО777Х799",power = 249,type = "SEDAN",price = 3500, available = True)
            car.save()        
    def Cars(self,request):
        try:
            cars=Car.objects.all()
            serializer=CarSerializer(cars,many=True)
            return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False,json_dumps_params={'ensure_ascii': False})
        except Exception as e:
            return JsonResponse({'message': '{}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)  
    def ACar(self,request,pk=None):
        try:       
            rental=Car.objects.get(id=pk)
            serializer=CarSerializer(rental)
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'message':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)
    