from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from user.models import Users
from django.contrib.auth.forms import UserCreationForm


def userHome(request):
    return render(request,'user/userHome.html')
def userLogin(request):
    context = {}
    return render(request,'user/userLogin.html',context)
def userRegister(request):   
    form = UserCreationForm()
    context = {'form':form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'user/userRegister.html',context)
def registered(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        context = Users(name=name, address=address, contact=contact, email=email, password=password, confirmpassword=confirmpassword)
        context.save()
    return render(request,'user/userLogin.html',context)
def loggedIn(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        if User(name==name, password==password):
            return render(request,'user/userHome.html')
        else:
            return render(request,'user/userLogin.html')
        
    
