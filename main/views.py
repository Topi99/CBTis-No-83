from django.shortcuts import render
from carreras.models import Carrera
from django.views.generic import View

class Home(View):
	def get(self, request):
		template_name = 'main/home.html'
		carreras = Carrera.objects.all()

		context = {
			'carreras': carreras, 
		}

		return render(request, template_name, context)
