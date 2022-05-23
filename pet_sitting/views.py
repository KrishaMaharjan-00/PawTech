from django.shortcuts import render, redirect
from django.http import HttpResponse
from pet_sitting.models import PetSitting, PetSitter
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def userPetSitting(request):
    return render(request,'petsitting/userPetSitting.html')
def selectPetSitter(request):
    return render(request,'petsitting/selectPetSitter.html')
def applyForPetSitter(request):
    return render(request,'petsitting/applyforps.html')
def petSitterConfirm(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        age=request.POST.get('age')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        petexp=request.POST.get('petexp')
        context = PetSitter(name=name, address=address, age=age, contact=contact, email=email, petexp=petexp)
        context.save()
        send_mail(
            "Result Regarding Pet Sitter Application",
            "Thank you for your application for petsitter. We will review your application and if you are qualified then, we will add you in our page and our team members will contact you soon.",
            "your_email_address",
            [email],
            fail_silently=False,
        )
    return render(request,'petsitting/petsitterconfirm.html')
def petSittingConfirm(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        petname=request.POST.get('petname')
        # petphoto=request.POST.get('petphoto')
        petage=request.POST.get('petage')
        petbreed=request.POST.get('petbreed')
        petdescription=request.POST.get('petdescription')
        petfood=request.POST.get('petfood')
        petsittingreason=request.POST.get('petsittingreason')
        context = PetSitting(name=name, address=address, contact=contact, email=email, petname=petname, petage=petage, petbreed=petbreed, petdescription=petdescription, petfood=petfood, petsittingreason=petsittingreason)
        context.save()
        send_mail(
            "Confirmation Mail For Pet Sitting",
            "Thank you for your application for petsitting. We have stored your details, so you could bring your pets to the designated addresses of the petsitter and for further details you can communicate with them thereafter.",
            "your_email_address",
            [email],
            fail_silently=False,
        )
    return render(request,'petsitting/petsittingconfirm.html')
