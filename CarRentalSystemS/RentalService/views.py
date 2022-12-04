from django.http import JsonResponse
from .models import RentalService
from .serializers import RentalSerializer 
from rest_framework.response import Response
from rest_framework import status,viewsets

class RentalViewSet(viewsets.ViewSet):
    def Rent(self,request):
        try:
            serializer=RentalSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'message':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)
    