from django.http import JsonResponse
from .models import Rental
from .serializers import RentalSerializer 
from rest_framework.response import Response
from rest_framework import status,viewsets
from django.shortcuts import render
from pytz import timezone


class RentalViewSet(viewsets.ViewSet):
    
    def Rentals(self,request):
        try:
            rentals=Rental.objects.all()
            serializer=RentalSerializer(rentals,many=True)
            return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False,json_dumps_params={'ensure_ascii': False})
        except Exception as e:
            return JsonResponse({'message': '{}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
    def createRental(self,request):
        try:
            serializer=RentalSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            print('created')
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'message':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)
    def GetRental(self,request,reservationUid=None):
        try:       
            rental=Rental.objects.get(rental_uid = rental_uid)
            serializer=RentalSerializer(rental)
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'message':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)
    def cancelRental(self,request,rental_uid=None):
        try:
            reservation=Rental.objects.get(rental_uid=rental_uid)
            serializer=RentalSerializer(reservation,data=request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'message':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)