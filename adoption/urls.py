from django.urls import path
from django.contrib.auth import admin
from . import views

app_name = 'adoption' 

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('adoption',views.adoption, name='adoption'),
    path('adoptionform',views.adoptionform, name='adoptionform'),
    path('adoptconfirm',views.adoptconfirm, name='adoptconfirm'),
    
    
    
]
