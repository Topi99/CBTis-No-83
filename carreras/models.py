from django.db import models
from django.core.urlresolvers import reverse

class Carrera(models.Model):
	nombre = models.CharField(max_length=70)
	# desc = models.CharField(max_length=140)
	cuerpo = models.TextField()
	imagen = models.ImageField(upload_to="assets/carreras/", null=True, blank=True)

	def get_absolute_url(self):
		return reverse('carreras:detalle', args=[self.nombre])

	def get_desc(self):
		return self.cuerpo[:200]+"..."

	def __str__(self):
		return self.nombre

class Modulo(models.Model):
	nombre = models.CharField(max_length=70)
	carrera = models.ForeignKey(Carrera, related_name='modulos')
	imagen = models.ImageField(upload_to="assets/carreras/modulos/", null=True, blank=True)

	def __str__(self):
		return self.nombre

class SubModulo(models.Model):
	nombre = models.CharField(max_length=70)
	desc = models.TextField()
	modulo = models.ForeignKey(Modulo, related_name='submodulos')
	imagen = models.ImageField(upload_to="assets/carreras/modulos/", null=True, blank=True)

	def __str__(self):
		return self.nombre