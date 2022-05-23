from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
import sms

def adminHome(request):
    if request.method == 'POST':
        send_mail(
            "Seat Confirmation Mail",
            "We would like to notify you that the seat for rescue shelter you have been waiting for is available, now for the further process our team will call you soon.",
            "yeona.kim1230@gmail.com",
            ["dea.kim1230@gmail.com"],
            fail_silently=False,
        )

        with sms.get_connection() as connection:
            sms.Message(
                'We would like to notify you that the seat for rescue shelter you have been waiting for is available, now for the further process our team will call you soon.', '+12184439177', ['+9779840021911'],
                connection=connection
            ).send()
    return render(request,'admin/adminHome.html')
def adminLogin(request):
    return render(request,'admin/adminLogin.html')
def adminAdoption(request):
    return render(request,'admin/adminAdoption.html')
def adminAddnew(request):
    return render(request,'admin/adminAddnew.html')
def addRescueDetails(request):
    return render(request,'admin/addrescuedetails.html')
def adminRescue(request):
    return render(request,'admin/adminRescue.html')
def addAdoptionDetails(request):
    return render(request,'admin/addadoptiondetails.html')
def addPetSitterDetails(request):
    return render(request,'admin/addpetsitterdetails.html')
