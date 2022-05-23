from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('adminhome',views.adminHome, name='adminhome'),
    path('adminlogin',views.adminLogin, name='adminlogin'),
    path('adminadoption',views.adminAdoption, name='adminadoption'),
    path('adminaddnew',views.adminAddnew, name='adminaddnew'),
    path('adminrescue',views.adminRescue, name='adminrescue'),
    path('addrescuedetails',views.addRescueDetails, name='addrescuedetails'),
    path('addadoptiondetails',views.addAdoptionDetails, name='addadoptiondetails'),
    path('addpetsitterdetails',views.addPetSitterDetails, name='addpetsitterdetails'),
    
    
]
