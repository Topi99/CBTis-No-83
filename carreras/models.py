from django.db import models
from django.core.urlresolvers import reverse
from django_markdown.models import MarkdownField

class Carrera(models.Model):
	nombre = models.CharField(max_length=70)
	# desc = models.CharField(max_length=140)
	cuerpo = MarkdownField()
	imagen = models.ImageField(upload_to="assets/carreras/", null=True, blank=True)

	def get_absolute_url(self):
		return reverse('carreras:detalle', args=[self.nombre])

	def get_desc(self):
		return self.cuerpo[:200]+"..."

	def __str__(self):
		return self.nombre

class Modulo(models.Model):
	nombre = models.CharField(max_length=140)
	carrera = models.ForeignKey(Carrera, related_name='modulos')

	def __str__(self):
		return self.nombre[:3]

class SubModulo(models.Model):
	nombre = models.CharField(max_length=140)
	desc = MarkdownField()
	modulo = models.ForeignKey(Modulo, related_name='submodulos')
	imagen = models.ImageField(upload_to="assets/carreras/modulos/", null=True, blank=True)
	horas = models.IntegerField(blank=True, null=True)

	def get_desc(self):
		return self.desc[:200]+'...'

	def __str__(self):
		return self.nombre[:5]