# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    is_estudiante = models.BooleanField(default=False)
    is_docente = models.BooleanField(default=False)

    def __str__(self):
        return self.username
        
class PerfilEstudiante(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class PerfilDocente(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Clase(models.Model):
    name = models.CharField(max_length=100)
    estudiantes = models.ManyToManyField(PerfilEstudiante, related_name='clases')
    docente = models.ForeignKey(PerfilDocente, on_delete=models.CASCADE, related_name='clases')
    def __str__(self):
        return self.name + " - " + self.docente.name

class Publicacion(models.Model):
    content = models.TextField()
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='publicaciones')
    docente = models.ForeignKey(PerfilDocente, on_delete=models.CASCADE, related_name='publicaciones')
    def __str__(self):
        return self.clase.name + " - " + self.content

class Asignacion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='asignaciones')
    def __str__(self):
        return self.title + " - " + self.clase.name + " - " + self.due_date.strftime('%Y-%m-%d %H:%M:%S')

class Entrega(models.Model):
    asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE, related_name='entregas')
    estudiante = models.ForeignKey(PerfilEstudiante, on_delete=models.CASCADE, related_name='entregas')
    file = models.FileField(upload_to='entregas/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.asignacion.title + " - " + self.estudiante.name + " - " + self.submitted_at.strftime('%Y-%m-%d %H:%M:%S')
