from django.db import models
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse

class Articulo(models.Model):

	TIPOS = {
		('noticia', 'Noticia'),
		('institucion', 'Nuestra Institución'),
		('info_academica', 'Información Académica'),
		('extraescolares', 'Actividades Extraescolares'),
		('docentes_escolares', 'Servicios Docentes y Escolares'),
	}

	nombre = models.CharField(max_length=240)
	cuerpo = MarkdownField()
	imagen = models.ImageField(upload_to="assets/articulos/", null=True, blank=True)
	tipo = models.CharField(max_length=20, choices=TIPOS, default='noticia',blank=True,null=True)
	slug = models.SlugField(blank=True,null=True)

	def __str__(self):
		return self.nombre

	def desc(self):
		return self.cuerpo[:200]+'...'

	def get_absolute_url(self):
		return reverse('main:detail', args=[self.slug])