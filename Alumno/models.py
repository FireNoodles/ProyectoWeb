from django.db import models
from django.utils import timezone

class Alumno(models.Model):
	idAlumno = models.AutoField(primary_key=True)
	NombreAlumno = models.CharField(max_length=40,null=False)
	ApellidoParterno = models.CharField(max_length=40,null=False)
	ApellidoMarterno = models.CharField(max_length=40)
	Email = models.EmailField(max_length=250,null=False)
	Edad = models.IntegerField(null=False)
	Semestre = models.IntegerField(null=False)
	Carrera = models.CharField(max_length=100,null=False)
	Especialidad = models.CharField(max_length=100,null=False)
		
