# ----------------librerias------------
from rest_framework import routers, serializers, viewsets
from drf_dynamic_fields import DynamicFieldsMixin
# ----------------Modelos--------------
# Nombre app                      nombre modelo
from Profesor.models import Profesor

class ProfesorSerializers(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('__all__')