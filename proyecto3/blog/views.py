from django.http import HttpResponse
from django.shortcuts import render
from .models import Entrada
from .forms import FormularioEntrada
# Create your views here.
def index(request):
    entradas=Entrada.objects.all()
    return render(request, "blog.html",{"entradas":entradas})
def crea_entrada(request):
    form=FormularioEntrada()
    return render(request,"creaEntrada.html",{"form":form})