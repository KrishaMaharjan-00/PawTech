from django.urls import path
from . import views


app_name = 'user' 

urlpatterns = [
    # path('admin/', admin.site.urls)
    path('user',views.userHome, name='user'),
    path('userlogin',views.userLogin, name='userlogin'),
    path('register',views.userRegister, name='register'),
    path('registered',views.registered, name='registered'),
    path('loggedIn',views.loggedIn, name='loggedIn'),
    
    
]
