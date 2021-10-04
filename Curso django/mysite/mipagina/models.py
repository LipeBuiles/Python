from django.db import models

# Create your models here.

class Personas(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="La direccion")
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=11)

