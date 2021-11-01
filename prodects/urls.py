from django.urls import path
from . import views



urlpatterns = [
    path('prodects',views.prodects,name='prodects'),
    path('prodect',views.prodect,name='prodect'),
    
]