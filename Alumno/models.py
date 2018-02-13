from django.db import models
from django.utils import timezone

class Alumno(models.Model):
	idAlumno = models.AutoField(primary_key=True)
	NombreAlumno = models.CharField(max_length=40)
	ApellidoParterno = models.CharField(max_length=40)
	ApellidoMarterno = models.CharField(max_length=40)
	Email = models.EmailField(max_length=250)
	Edad = models.IntegerField()
	Semestre = models.IntegerField()
	Carrera = models.CharField(max_length=100)
	Especialidad = models.CharField(max_length=100)
		
