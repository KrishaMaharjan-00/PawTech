lfrom django.shortcuts import render, redirect
from django.http import HttpResponse
from rescue.models import Seats, Dogs
from django.core.mail import send_mail

def Rescue(request):
    return render(request,'rescue/rescueshelters.html')

def NotifyConfirm(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        context = Seats(email=email, phonenumber=phonenumber)
        context.save()
        send_mail(
            "Rescue Confirmation Mail",
            "We have received your appeal for rescue. But there is no available seat at the current moment, so we will mail and messaged you in case of seat availabilty.",
            "your_email_address",
            [email],
            fail_silently=False,
        )
    return render(request,'rescue/seatAvailable.html')

def RescueEmailForm(request):
    return render(request,'rescue/rescueEmailForm.html')

def RescuePet(request):
    return render(request,'rescue/rescuepet.html')


def RescueConfirm(request):
    if request.method == 'POST':
        dogdetails=request.POST.get('dogdetails')
        name=request.POST.get('name')
        address=request.POST.get('address')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        context = Dogs(dogdetails=dogdetails, name=name, address=address, contact=contact, email=email)
        context.save()
        send_mail(
            "Rescue Confirmation Mail",
            "We have received your appeal for rescue. Our team will call you soon regarding the next details, so please stay in touch.",
            "email_address",
            [email],
            fail_silently=False,
        )
    return render(request,'rescue/rescueConfirm.html')
