from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)

