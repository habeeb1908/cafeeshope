from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signin(request):
    return render(request,'accounts/signin.html')

def singup(request):
    return render(request,'accounts/singup.html')   

def profile(request):
    return render(request,'accounts/profile.html')      

   