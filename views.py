from django.shortcuts import render

# Create your views here.

# app/views.py

from django.shortcuts import render

def index(request):
    return render(request,'app/index.html')

def dashboard(request):

    return render(request,'dashboard.html')

def clientes(request):
    return render(request,'clientes.html')

def suscripciones(request):
    return render(request,'suscripciones.html')

def facturas(request):
    return render(request,'facturas.html')

def montos(request):
    return render(request,'montos.html')

