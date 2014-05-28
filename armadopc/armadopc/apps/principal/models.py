from django.db import models

# Create your models here.
class Nuevousuario(models.Model):
	nombre=models.CharField(max_length=100)
	apellido=models.CharField(max_length=100)
	ci=models.CharField(max_length=11)
	email=models.EmailField()
	fecha_ingreso=models.DateField()
	def __unicode__(self):
		return self.nombre
