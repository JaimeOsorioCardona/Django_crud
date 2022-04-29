from turtle import home
from django.urls import path
from . import views

urlpatterns =[
    path('', views.home),
    path('plato/', views.plato),
    path('registrarplatos/', views.registrarplatos),
    path('registraralimentos/', views.registraralimentos),
    path('alimentos/',views.ingredientes),
    path('eliminarplatos/<codigo>',views.eliminarplatos),
    path('eliminaralimentos/<codigo>',views.eliminaralimientos),
    path('editarplatos/<codigo>', views.editarplatos),
    path('editaralimentos/<codigo>', views.editaralimentos),
    path('edicionplatos/', views.edicionplatos),
    path('edicionalimentos/', views.edicionalimentos),
]