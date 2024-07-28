from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(AppUser)
admin.site.register(PerfilEstudiante)
admin.site.register(PerfilDocente)
admin.site.register(Clase)
admin.site.register(Publicacion)
admin.site.register(Asignacion)
admin.site.register(Entrega)

