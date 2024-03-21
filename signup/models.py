from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.CharField(max_length=35,unique=True)
    