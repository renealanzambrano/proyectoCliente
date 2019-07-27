from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . import views

urlpatterns = [
    re_path(r'^alumno1/$', views.AlumnoList.as_view()),
    re_path(r'^alumno1/(?P<pk>\d+)$', views.AlumnoDetail.as_view()),
]