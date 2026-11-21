from django.db import models
from django.contrib.auth.models import User

class Playa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    imagen = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.nombre

class Resena(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    playa = models.ForeignKey(Playa, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.playa.nombre}"