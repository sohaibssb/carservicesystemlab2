import json
from django.shortcuts import render
import requests
from django.core.paginator import Paginator
from django.core import serializers
from rest_framework import viewsets,status
from rest_framework.response import Response
from django.http import JsonResponse
import json
from datetime import datetime
from time import sleep
from django.shortcuts import redirect
import time
class GatewayViewSet(viewsets.ViewSet):
    
 
    def BookCar(self,request):
        try:
            username=request.headers['X-User-Name']
            cars=requests.get('http://carsservice:8070/api/v1/cars')
            for car in cars.json():
                if car['car_uid']==request.data['car_uid']:
                    choosedCar=car
                    break
            d1 = datetime.strptime(request.data['date_from'], "%Y-%m-%d")
            d2 = datetime.strptime(request.data['date_to'], "%Y-%m-%d")
            days=d1-d2
            price=car['price']*days.days
            cost=price
            payment=requests.post('http://paymentservice:8050/api/v1/Payment',json={'status':'PAID','price':cost})
            data={'username':username['username'],'paymentUid':payment.json()['paymentUid'],'car_uid':choosedCar['id'],'status':'PAID','date_from':request.data['date_from'],'date_to':request.data['date_to']}
            rental=requests.post('http://rentalservice:8060/api/v1/rentals',data=data)
            data={'rental_uid':rental.json()['rental_uid'],'car_uid':choosedCar['car_uid'],'date_from':rental.json()['date_from'],'date_to':rental.json()['date_to'],'status':rental.json()['status'],'payment':payment.json()}
            return JsonResponse(data,status=status.HTTP_200_OK,safe=False,json_dumps_params={'ensure_ascii': False})
        except Exception as e:
            return JsonResponse({'message':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)
    
    def GetInfoUser(self,request):
        try:
            
            username=request.headers['X-User-Name']
            rentals=requests.get('http://rentalservice:8060/api/v1/rentals')
            userRentals=[rental for rental in rentals.json() if rental['username']==username]
            
            cars=requests.get('http://carsservice:8070/api/v1/cars')
            payments=requests.get('http://paymentservice:8050/api/v1/Payment')
            infosUser=[]
            for rental in userRentals:
                for car in cars.json():
                    if car['id']==rental['car_uid']:
                        reservedCar=car
                        break
                for paymen in payments.json():
                    if paymen['paymentUid']==rental['paymentUid']:
                        payment=paymen
                        break
                reservedCar['fullAddress']=reservedCar['brand']+', '+reservedCar['model']+', '+reservedCar['registration_number']
                data={'rental_uid':rental['rental_uid'],'car':reservedCar,'date_from':rental['date_from'],'date_to':rental['date_to'],'status':rental['status'],'payment':payment}
                infosUser.append(data)
            return JsonResponse({'rentals':infosUser},status=status.HTTP_200_OK,safe=False,json_dumps_params={'ensure_ascii': False})
        except Exception as e:
            return JsonResponse({'message':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)

    def UserSpecificRental(self,request,rental_uid=None):
        username=request.headers['X-User-Name']
        rental=requests.get('http://rentalservice:8060/api/v1/rentals/{}'.format(rental_uid))
        car=requests.get('http://carsservice:8070/api/v1/cars/{}'.format(rental.json()['car_uid']))
        payment=requests.get('http://paymentservice:8050/api/v1/Payment/{}'.format(rental.json()['paymentUid']))
        cardict=car.json()
        cardict['fullAddress']=car.json()['brand']+', '+car.json()['model']+', '+car.json()['registration_number']
        if rental.json()['username']!=username:
            return JsonResponse({'message':'je sais pas'},status=status.HTTP_400_BAD_REQUEST)
        data={'rental_uid':rental.json()['rental_uid'],'car':cardict,'car_uid':car.json()['car_uid'],'date_from':rental.json()['date_from'],'date_to':rental.json()['date_to'],'status':rental.json()['status'],'payment':payment.json()}
        return JsonResponse(data,status=status.HTTP_200_OK,safe=False,json_dumps_params={'ensure_ascii': False})

    def cars(self,request):
        
        cars=requests.get('http://carsservice:8070/api/v1/cars')
        paginator = Paginator(cars.json(), request.GET.get('size'))
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if cars.status_code != 200:
            return JsonResponse({'message':'je sais pas'},status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'items':cars.json(),"totalElements":len(cars.json()),"page":request.GET.get('page'),"pageSize":int(request.GET.get('size'))},status=status.HTTP_200_OK,safe=False,json_dumps_params={'ensure_ascii': False})
    
        
    def UserRentals(self,request):
        try:
            username=request.headers['X-User-Name']
            rentals=requests.get('http://rentalservice:8060/api/v1/rentals')
            userRentals=[rental for rental in rentals.json() if rental['username']==username]
            infoUserRentals=[]
            cars=requests.get('http://carsservice:8070/api/v1/cars')
            payments=requests.get('http://paymentservice:8050/api/v1/Payment')
            for rental in userRentals:
                for car in cars.json():
                    if car['id']==rental['car_uid']:
                        reservedCar=car
                        break
                for paymen in payments.json():
                    if paymen['paymentUid']==rental['paymentUid']:
                        payment=paymen
                reservedCar['fullAddress']=reservedCar['brand']+', '+reservedCar['model']+', '+reservedCar['registration_number']
                data={'rental_uid':rental['rental_uid'],'car':reservedCar,'date_from':rental['date_from'],'date_to':rental['date_to'],'status':rental['status'],'payment':payment}
                infoUserRentals.append(data)
            return JsonResponse(infoUserRentals,status=status.HTTP_200_OK,safe=False,json_dumps_params={'ensure_ascii': False})
        except Exception as e:
            return JsonResponse({'message':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)
    
    def cancelRental(self,request,rental_uid=None):
        try:
            username=request.headers['X-User-Name']
            rental=requests.patch('http://rentalservice:8060/api/v1/rentals/{}'.format(rental_uid),data={'status':'CANCELED'})
            if rental.json()['username']==username:
                payment=requests.patch('http://paymentservice:8050/api/v1/Payment/{}'.format(rental.json()['paymentUid']),data={'status':'CANCELED'})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
