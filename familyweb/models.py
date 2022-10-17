from django.db import models
from django.utils.timezone import now

class families(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_registro = models.DateTimeField(default=now)