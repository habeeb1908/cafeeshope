from django.shortcuts import render

# Create your views here.
def prodects(request):
    return render(request,'prodects/prodects.html')
def prodect(request):
    return render(request,'prodects/prodect.html')    

def search(request):
    return render(request,'prodects/search.html')        