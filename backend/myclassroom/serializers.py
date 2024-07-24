from rest_framework import serializers
from .models import Clase, Entrega, Publicacion, PerfilEstudiante, PerfilDocente, Asignacion, AppUser


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['username', 'password', 'is_estudiante', 'is_docente']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Create the AppUser instance
        user = AppUser.objects.create_user(**validated_data)
        
        # Check if the user is a student or a teacher
        if user.is_estudiante:
            PerfilEstudiante.objects.create(user=user)
        if user.is_docente:
            PerfilDocente.objects.create(user=user)

        return user


class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['id', 'content']
class PerfilDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilDocente
        fields = ['id', 'name']

class PerfilEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilEstudiante
        fields = ['id', 'name']
class AsignacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Asignacion
    fields = ["id", "title", "description"]
    
class RegisterPublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['id', 'content', 'clase', 'docente']

class RegisterEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrega
        fields = ['id', 'asignacion', 'estudiante', 'file', 'submitted_at']

class RegisterAsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignacion
        fields = ['id', 'title', 'description', 'due_date', 'clase']

class RegisterClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['id', 'name', 'estudiantes', 'docente']

    
class EntregaSerializerAlDocente(serializers.ModelSerializer):
  estudiante = PerfilEstudianteSerializer()
  asignacion = AsignacionSerializer()
  class Meta:
    model = Entrega
    fields = ['id', 'file', 'submitted_at', 'estudiante', 'asignacion']
        

class ClaseSerializerAlDocente(serializers.ModelSerializer):
  entregas = serializers.SerializerMethodField()
  publicaciones = PublicacionSerializer(many=True, read_only=True)
  estudiantes = PerfilEstudianteSerializer(many=True, read_only=True)
  
  class Meta:
      model = Clase
      fields = ['id', 'name', 'entregas', 'publicaciones', 'estudiantes']
  def get_entregas(self, obj):
    asignaciones = Asignacion.objects.filter(clase=obj)
    return EntregaSerializerAlDocente(Entrega.objects.filter(asignacion__in=asignaciones), many=True).data
        
class ClaseSerializerAlEstudiante(serializers.ModelSerializer):
  docente = PerfilDocenteSerializer(read_only = True)
  publicaciones = PublicacionSerializer(many=True, read_only=True)
  estudiantes = PerfilEstudianteSerializer(many=True, read_only=True)
  asignaciones = AsignacionSerializer(many=True, read_only=True)
  class Meta:
    model = Clase
    fields = ['docente', 'publicaciones', 'estudiantes', 'asignaciones']