from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('about',views.about, name='about'),
    path('gallery',views.userGallery, name='gallery'),
    path('contact',views.contact, name='contact'),
    path('donation',views.donation, name='donation'),
    
]
