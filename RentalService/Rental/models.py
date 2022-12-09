from django.db import models
import uuid
from datetime import date
import time

class Rental(models.Model):
    rental_uid = models.UUIDField(default=uuid.uuid4,unique=True,editable=True)
    username = models.CharField(max_length=80)
    payment_uid = models.UUIDField(default=uuid.uuid4,unique=True,editable=True)
    car_uid = models.UUIDField(default=uuid.uuid4,unique=True,editable=True)
    date_from = date.fromtimestamp(time.time())
    date_to = date.fromtimestamp(time.time())
    status = models.CharField(max_length=20)

    
    

  