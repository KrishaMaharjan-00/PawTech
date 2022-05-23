from django.urls import path
from . import views

app_name = 'rescue'

urlpatterns = [
    # path('admin/', admin.site.urls)
    path('rescue',views.Rescue, name='rescue'),
    path('notifyconfirm',views.NotifyConfirm, name='notifyconfirm'),
    path('rescueemailform',views.RescueEmailForm, name='rescueemailform'),
    path('rescuepet',views.RescuePet, name='rescuepet'),
    path('rescueconfirm',views.RescueConfirm, name='rescueconfirm'),
    
    
]