from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Carrera

class DetailCarrera(View):
	def get(self, request, nombre):
		template_name = 'carreras/detail.html'
		carrera = get_object_or_404(Carrera, nombre=nombre)
		context = {
			'carrera':carrera,
		}

		return render(request, template_name, context)
