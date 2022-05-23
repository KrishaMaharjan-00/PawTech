from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import adoption
# from .models import admin



# Create your views here.
def home(request):
    return render(request,'MainPage.html')
def about(request):
    return render(request,'about.html')
def userGallery(request):
    return render(request,'userGallery.html')
def contact(request):
    return render(request,'contact.html')
def donation(request):
    return render(request,'donation.html')



