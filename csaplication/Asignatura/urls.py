from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from Asignatura import views

urlpatterns = [
    re_path(r'^asignatura1/$', views.AsignaturaList.as_view()),
    re_path(r'^asignatura1/(?P<pk>\d+)$', views.AsignaturaDetail.as_view()),
]