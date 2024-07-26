# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    is_estudiante = models.BooleanField(default=False)
    is_docente = models.BooleanField(default=False)
        
class PerfilEstudiante(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
class PerfilDocente(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Clase(models.Model):
    name = models.CharField(max_length=100)
    estudiantes = models.ManyToManyField(PerfilEstudiante, related_name='clases')
    docente = models.ForeignKey(PerfilDocente, on_delete=models.CASCADE, related_name='clases')

class Publicacion(models.Model):
    content = models.TextField()
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='publicaciones')
    docente = models.ForeignKey(PerfilDocente, on_delete=models.CASCADE, related_name='publicaciones')

class Asignacion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='asignaciones')

class Entrega(models.Model):
    asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE, related_name='entregas')
    estudiante = models.ForeignKey(PerfilEstudiante, on_delete=models.CASCADE, related_name='entregas')
    file = models.FileField(upload_to='entregas/')
    submitted_at = models.DateTimeField(auto_now_add=True)
