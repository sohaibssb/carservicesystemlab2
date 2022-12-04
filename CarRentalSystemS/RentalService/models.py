from django.db import models
import uuid
from datetime import date
import time

class RentalService(models.Model):
    rental_uid = uuid.uuid4()
    username = models.CharField(max_length=80)
    payment_uid = uuid.uuid1()
    car_uid = models.UUIDField()
    date_from = date.fromtimestamp(time.time())
    date_to = date.fromtimestamp(time.time())
    status = models.CharField(max_length=20)
    

   
    def get_info(self):
        return self.rental_uid+' '+str(self.username)+' '+self.payment_uid+' '+self.car_uid

    def __str__(self):
        return self.rental_uid+' '+str(self.id)
 