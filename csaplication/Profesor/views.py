#-----------------------LIBRERIAS-----------------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

#-----------------------MODELOS-------------------------
from Profesor.models import Profesor
#--------------------SERIALIZERS--------------------------
from Profesor.serializers import ProfesorSerializers

class ProfesorList(APIView):
    def get(self, request, format=None):
        queryset = Profesor.objects.all()
        serializer = ProfesorSerializers(queryset, many=True, context = {'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfesorSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response (datas)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

class ProfesorDetail(APIView):
    # METODO CONSULTAR EL ID Y ME RETORNE SI EXISTE O NO
    def get_object(self, id):
        try:
            return Profesor.objects.get(pk=id)
        except Profesor.DoesNotExist:
            return "No"

    # METODO CONSULTAR EL ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
    def get(self, request, id, format=None):
        teacher1 = self.get_object(id)
        serializer = ProfesorSerializers(teacher1)
        return Response(serializer.data)
    
    # METODO CONSULTAR EL ID Y ACTULIZAR LOS VALORES DE SUS CAMPOS
    def put(self, request, id, format=None):
        teacher1 = self.get_object(id)
        serializer = ProfesorSerializers(teacher1, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #METODO DE ELIMINACION
    def delete(self, request, id, format=None):
        teacher1 = self.get_object(id)
        serializer = ProfesorSerializers(teacher1, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
