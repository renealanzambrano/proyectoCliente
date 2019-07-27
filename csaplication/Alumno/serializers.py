# ----------------librerias------------
from rest_framework import routers, serializers, viewsets
from drf_dynamic_fields import DynamicFieldsMixin
# ----------------Modelos--------------
# Nombre app                      nombre modelo
from Alumno.models import Alumno

class AlumnoSerializers(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('__all__')