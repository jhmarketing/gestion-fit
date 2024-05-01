from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    repeticiones = models.CharField(max_length=100)
    parte_trabajada = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.nombre

class PlanEntrenamiento(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    persona = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planes_creados')
    ejercicios = models.ManyToManyField(Ejercicio, related_name='planes')
