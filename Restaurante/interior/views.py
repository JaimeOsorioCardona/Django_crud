from django.shortcuts import render
from .models import platos, alimentos
from django.shortcuts import redirect, render
from sre_constants import CATEGORY_UNI_SPACE

# Create your views here.

def home(request):
    return redirect('/plato')

def plato(request):
    plato = platos.objects.all()
    ingredientes = alimentos.objects.all()
    return render(request,"gestionplatos.html",{"platos":plato,"alimentos":ingredientes})

def ingredientes(request):
    ingredientes = alimentos.objects.all()
    return render(request,"gestionalimentos.html",{"alimentos":ingredientes})

def registrarplatos(request):
    alimento = alimentos.objects.get(codigoA=request.POST['codigoA_ingredientes'])
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    tiempo_de_preparacion=request.POST['tiempo_de_preparacion']
    categoria=request.POST['txtcategoria']
    ingredientes=alimento
    plato = platos.objects.create(codigo=codigo, nombre=nombre, tiempo_de_preparacion=tiempo_de_preparacion, categoria=categoria,ingredientes=ingredientes)
    return redirect('/plato')
    
def registraralimentos(request):
    codigoA = request.POST['txtcodigoA']
    nombre = request.POST['txtnombre']
    categoria = request.POST['txtcategoria']
    alimentos.objects.create(codigoA=codigoA, nombre=nombre, categoria=categoria)
    return redirect('/alimentos')

def eliminarplatos(request,codigo):
    plato = platos.objects.get(codigo=codigo)
    plato.delete()
    return redirect('/plato')

def eliminaralimientos(request,codigo):
    alimento = alimentos.objects.get(codigoA=codigo)
    alimento.delete()
    return redirect('/alimentos')

def editarplatos(request,codigo):
    plato = platos.objects.get(codigo=codigo)
    ingredientes = alimentos.objects.all()
    return render(request, "editarplatos.html", {"plato": plato , "alimentos":ingredientes})

def editaralimentos(request,codigo):
    alimento = alimentos.objects.get(codigoA=codigo)
    return render(request, "editaralimentos.html", {"alimentos": alimento})

def edicionplatos(request):
    alimento = alimentos.objects.get(codigoA=request.POST['codigoA_ingredientes'])
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    tiempo_de_preparacion=request.POST['tiempo_de_preparacion']
    categoria=request.POST['txtcategoria']
    ingredientes=alimento

    plato = platos.objects.get(codigo=codigo)
    plato.codigo = codigo
    plato.nombre = nombre
    plato.tiempo_de_preparacion = tiempo_de_preparacion
    plato.categoria = categoria
    plato.ingredientes = ingredientes
    plato.save()
    return redirect('/plato')

def edicionalimentos(request):
    codigoA = request.POST['txtcodigoA']
    nombre = request.POST['txtnombre']
    categoria = request.POST['txtcategoria']

    alimento = alimentos.objects.get(codigo=codigoA)
    alimento.codigoA = codigoA
    alimento.nombre = nombre
    alimento.categoria = categoria
    alimento.save()
    return redirect('/alimentos')