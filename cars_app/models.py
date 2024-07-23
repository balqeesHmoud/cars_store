from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    model = models.CharField(max_length=100, null=False, blank=False)
    brand = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    is_bought = models.BooleanField(default=False, null=False, blank=False)
    buyer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    buy_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"
