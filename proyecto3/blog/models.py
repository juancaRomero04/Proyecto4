from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre=models.CharField(max_length=100, null=False, unique=True, verbose_name='Nombre')
    def __str__(self):
        return self.nombre
    class Meta:
        db_table='categorias'
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['id']

class Entrada (models.Model):
    autor=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name='Titulo')
    contenido=models.TextField(null=True, verbose_name='Contenido')
    imagen=models.ImageField(upload_to='entradas/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    fecha_alta=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')
    fecha_actualizacion=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualizacion')

    def __str__(self):
        return self.titulo
    class Meta:
        db_table='entradas'
        verbose_name='Entrada'
        verbose_name_plural='Entradas'
        ordering=['id']
# Create your models here.
