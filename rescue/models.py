from django.db import models

# Create your models here.
class Seats(models.Model):
    email = models.EmailField(max_length=100)
    phonenumber = models.CharField(max_length=100)


class Dogs(models.Model):
    dogdetails = models.TextField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
