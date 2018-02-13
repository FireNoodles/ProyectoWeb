from django.db import models
from django.utils import timezone

class Maestro(models.Model):
	idMaestro = models.AutoField(primary_key=True)
	Nombre = models.CharField(max_length=30,null=False)
	ApellidoPaterno = models.CharField(max_length=30, null=False)
	ApellidoMaterno = models.CharField(max_length=30)
	

