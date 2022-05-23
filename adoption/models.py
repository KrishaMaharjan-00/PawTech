from django.db import models

# Create your models here.
class Adopt(models.Model):

    name = models.CharField(max_length=150)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=200)
    emailid = models.CharField(max_length=150)
    dogname = models.CharField(max_length=150)
    reason = models.TextField()