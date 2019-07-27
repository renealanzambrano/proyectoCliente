from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . import views

urlpatterns = [
    re_path(r'^profesor1/$', views.ProfesorList.as_view()),
    re_path(r'^profesor1/(?P<pk>\d+)$', views.ProfesorDetail.as_view()),
]