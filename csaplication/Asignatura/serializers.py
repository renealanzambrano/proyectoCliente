# ----------------librerias------------
from rest_framework import routers, serializers, viewsets
from drf_dynamic_fields import DynamicFieldsMixin
# ----------------Modelos--------------
# Nombre app                      nombre modelo
from Asignatura.models import Asignatura

class AsignaturaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ('__all__')