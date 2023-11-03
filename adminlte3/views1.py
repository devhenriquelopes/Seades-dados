from django.shortcuts import render, redirect, get_object_or_404
from .models import Municipio, Cisternas, 
from .forms import MunicipioForm, CisternasForm
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    template_name = 'adminlte/municipio.html'
    context_object_name = 'municipio_list'
    
    
    def get_queryset(self):
        
        return Municipio.objects.all()

class IndexView3(ListView):
    template_name = 'adminlte/municipio.html'
    context_object_name = 'count'

    def get_queryset(self):  
        
        return Municipio.objects.count()


class EntregaSISAView(ListView):
    template_name = 'adminlte/sisa.html'
    context_object_name = 'EntregaSISA'

entregasSISA ===== 

entregasSISA.municipio = Municipio.objects.count()
ObjetentregasSISAox.alimenteos = Municipio.objects.count()
entregasSISA.EntregasLeite
entregasSISA.Refeicoes

    def get_queryset(self):
              return entregasSISA

class IndexView2(ListView):
    template_name = 'adminlte/sisa.html'
    context_object_name = 'cisternas_list'
    
    def get_queryset(self):
        return Cisternas.objects.all()        


