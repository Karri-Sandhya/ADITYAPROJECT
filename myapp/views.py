import copy
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def register(request):
    return render(request,'register.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def shop(request):
    return render(request,'shop.html')

def shopcopy(request):
    return render(request,'shopcopy.html')

def jewellery(request):
    return render(request,'jewellery.html')
