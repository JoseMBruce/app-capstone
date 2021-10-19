from django.db import models

# Create your models here.
class Auto(models.Model):
    patente = models.CharField(max_length=8)
    estado = models.CharField(max_length=20)
    tiempo_restante = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patente