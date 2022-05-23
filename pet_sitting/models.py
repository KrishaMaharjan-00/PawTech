from django.db import models
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s", (timeNow, filename)
    return os.path.join('uploads/', filename)


# Create your models here.
class PetSitting(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    petname = models.CharField(max_length=100)
    # petphoto = models.ImageField(upload_to=filepath, null=True, blank=True)
    petage = models.CharField(max_length=100)
    petbreed = models.CharField(max_length=100)
    petdescription = models.TextField()
    petfood = models.CharField(max_length=100)
    petsittingreason = models.TextField()

class PetSitter(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    petexp = models.TextField()
    