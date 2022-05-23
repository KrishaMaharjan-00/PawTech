from django.shortcuts import render, redirect
from django.http import HttpResponse
from adoption.models import Adopt
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages

def adoption(request):
    return render(request,'adoption/userAdoption.html')
def adoptionform(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        contact=request.POST.get('contact')
        emailid=request.POST.get('emailid')
        dogname=request.POST.get('dogname')
        reason=request.POST.get('reason')
        context = Adopt(name=name, address=address, contact=contact, emailid=emailid, dogname=dogname, reason=reason)
        context.save()
        send_mail(
            "Adoption Confirmation Mail",
            "Thank you for your application for adoption. Our team will reach you soon, so please stay in touch.",
            "yeona.kim1230@gmail.com",
            [emailid],
            fail_silently=False,
        )
        messages.info(request, 'Your password has been changed successfully!')
    return render(request,'adoption/userAdoptForm.html')
def adoptconfirm(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        contact=request.POST.get('contact')
        emailid=request.POST.get('emailid')
        dogname=request.POST.get('dogname')
        reason=request.POST.get('reason')
        context = Adopt(name=name, address=address, contact=contact, emailid=emailid, dogname=dogname, reason=reason)
        context.save()
        send_mail(
            "Adoption Confirmation Mail",
            "Thank you for your application for adoption. Our team will reach you soon, so please stay in touch.",
            "yeona.kim1230@gmail.com",
            [emailid],
            fail_silently=False,
        )

    return render(request,'adoption/adoptConfirm.html')

