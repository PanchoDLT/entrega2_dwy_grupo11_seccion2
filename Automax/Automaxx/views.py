from django.shortcuts import render
from .models import Slider,Galeria,MisionyVision
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_auth
from django.contrib.auth.decorators import login_required

def Pagina_inicio(request):
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    return render(request, 'web/Pagina_inicio.html', {'slider':slider, 'first':sliderFirst, 'last':sliderLast})
    
def galeria(request):
    gale = Galeria.objects.all()
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    return render(request,'web/galeria.html',{'gale':gale, 'slider':slider, 'first':sliderFirst, 'last':sliderLast})


def Mapa(request):
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    return render(request, 'web/Mapa.html', {'slider':slider, 'first':sliderFirst, 'last':sliderLast})

def Quienes_somos(request):
    misionyvision = MisionyVision.objects.first()
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    return render(request, 'web/Quienes_somos.html', {'slider':slider, 'first':sliderFirst, 'last':sliderLast, 'misionyvision':misionyvision})

def Registro_insumos(request):
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    return render(request, 'web/Registro_insumos.html', {'slider':slider, 'first':sliderFirst, 'last':sliderLast})

def Registro(request):
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    return render(request, 'web/Registro.html', {'slider':slider, 'first':sliderFirst, 'last':sliderLast})

def Base(request):
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    return render(request, 'web/Base.html', {'slider':slider, 'first':sliderFirst, 'last':sliderLast})

def logout_vista(request):
    logout(request)
    return render(request,'web/Pagina_inicio.html')

def login(request):
    if request.POST:
        Usuario = request.POST.get("nombreuser")
        password = request.POST.get("contrasena")
        us = authenticate(request,username=Usuario,password=password )
        if us is not None and us.is_active:
            login_auth(request,us)
            return render(request,'web/Pagina_inicio.html',{'user':us})
        else:
            return render(request,'web/login.html',{'msg':'usuario / contraseña invalido'})
    return render(request,'web/login.html' )
