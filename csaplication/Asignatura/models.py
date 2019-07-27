from django.db import models
from django.shortcuts import render
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Asignatura(models.Model):
    name= models.CharField(max_length=50, null=True)
    horario=models.CharField(max_length=50, null=True)
    created=models.DateTimeField(default = timezone.now)
    
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Asignatura'