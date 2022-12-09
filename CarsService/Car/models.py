from django.db import models
import uuid

class Car(models.Model):
    car_uid = models.UUIDField(default=uuid.uuid4,unique=True,editable=True)
    brand = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    registration_number = models.CharField(max_length=20)
    power = models.IntegerField()
    price = models.IntegerField()
    type = models.CharField(max_length=20)
    availability = models.BooleanField()

    def __str__(self):
        return self.brand
