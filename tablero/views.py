from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, FormView, View, DeleteView
from django.urls import reverse, reverse_lazy
import requests
import pymsgbox
from django.template import Context
from recep.models import Habitacion
from api.views import HabitacionViewSet
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

@login_required
def appTablero(request):
    responseHab = requests.get('http://127.0.0.1:8000/api/habitaciones/')
    responseList = responseHab.json()
    habitacionList = responseList
    contexto  = {"habitacionList": habitacionList}
    
    return render(request,"tablero.html", contexto)


@login_required
def registrarHabitacion(request):
    form = HabitacionForm()

    if request.method == "POST":
        print(request.POST)
        form = HabitacionForm(request.POST) 

        if form.is_valid():
            print("Valido")
            
            habitacion = Habitacion()

            habitacion.numero = form.cleaned_data['numero']
            habitacion.estado = form.cleaned_data['estado']
            habitacion.id_tipoHabitacion = form.cleaned_data['id_tipoHabitacion']

            habitacion.save()
    
        else:
            print("Invalido")

    return render(request, 'formHabitacion.html', {'form': form})



@login_required
def editarHabitacion(request, pk):
    
    habitacion = get_object_or_404(Habitacion, id=pk)

    form = HabitacionForm(initial={'numero':habitacion.numero,'estado':habitacion.estado, 'id_tipoHabitacion': habitacion.id_tipoHabitacion})

    if request.method == "POST":
        print(request.POST)
        form = HabitacionForm(request.POST) 

        if form.is_valid():
            print("Valido")

            habitacion.numero = form.cleaned_data['numero']
            habitacion.estado = form.cleaned_data['estado']
            habitacion.id_tipoHabitacion = form.cleaned_data['id_tipoHabitacion']

            habitacion.save()
            return redirect('appTablero')
    
        else:
            print("Invalido")
        
    return render(request, 'formHabitacion.html', {'form': form})



def eliminarHabitacion(request, id):
    habitacion = Habitacion.objects.get(id=id)
    habitacion.delete()
    return redirect('appTablero')

@login_required
def crearTipo(request):
    form = TipoHabitacionForm()

    if request.method == "POST":
        print(request.POST)
        form = TipoHabitacionForm(request.POST) 

        if form.is_valid():
            print("Valido")
            
            tipoHabitacion = TipoHabitacion()

            tipoHabitacion.tipo = form.cleaned_data['tipo']
            tipoHabitacion.precio = form.cleaned_data['precio']
            tipoHabitacion.descripcion = form.cleaned_data['descripcion']

            tipoHabitacion.save()
    
        else:
            print("Invalido")

    return render(request, 'formHabitacion.html', {'form': form})