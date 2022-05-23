from django.urls import path
from . import views

app_name='pet_sitting'

urlpatterns = [
    # path('admin/', admin.site.urls)
    path('petsitting',views.userPetSitting, name='petsiting'),
    path('selectpetsitting',views.selectPetSitter, name='selectpetsitting'),
    path('petsittingconfirm',views.petSittingConfirm, name='petsittingconfirm'),
    path('petsitterconfirm',views.petSitterConfirm, name='petsitterconfirm'),
    path('applyforps',views.applyForPetSitter, name='applyforps'),
    
    
]
