from msilib.schema import Class
from pyexpat import model
from django.db import models

# Create your models here.

class platos(models.Model):
    codigo= models.CharField(primary_key=True, max_length=3)
    nombre= models.CharField(max_length=50)
    tiempo_de_preparacion = models.IntegerField(default=60)
    categoria = models.CharField(max_length=30,default="comida")
    ingredientes = models.ForeignKey('alimentos',on_delete=models.CASCADE,default=0)

class alimentos(models.Model):
    codigoA= models.CharField(primary_key=True, max_length=2)
    nombre= models.CharField(max_length=40)
    categoria = models.CharField(max_length=30)
