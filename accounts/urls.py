from django.urls import path
from . import views

urlpatterns = [
    path('singnin',views.signin, name='singin'),
    path('singup',views.singup, name='singup'),
     path('profile',views.profile, name='profile'),
   

    
    
]