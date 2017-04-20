from django.shortcuts import render
from carreras.models import Carrera
from django.views.generic import View
from .models import Articulo

class Home(View):
	def get(self, request):
		template_name = 'main/home.html'
		carreras = Carrera.objects.all()
		nombres_carr = []
		posts_institucion = Articulo.objects.filter(tipo='institucion')

		for n in carreras:
			nombres_carr.append(n)

		context = {
			'names_carr': nombres_carr, 
			'posts_institucion':posts_institucion,
		}

		return render(request, template_name, context)

class DetailPost(View):
	def get(self, request, slug):
		template_name = 'articulos/detail.html'
		# post = get_object_or_404(Articulo, slug=slug)
		post = Articulo.objects.get(slug=slug)

		context = {
			'post':post,
		}

		return render(request, template_name, context)
