from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Customer(AbstractUser):
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.username


class Address(models.Model):
    customer = models.ForeignKey(Customer, related_name='address', on_delete=models.CASCADE)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    country = models.CharField(max_length=300)

    def __str__(self):
        return 'Address {}'.format(self.id)
