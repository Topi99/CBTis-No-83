from django import template
from ..models import Articulo

register = template.Library()

@register.inclusion_tag('articulos/posts_tipo.html')
def posts_tipo(tipo):
	posts = Articulo.objects.filter(tipo=tipo)
	posts_l = list(posts[:6])
	return {'posts':posts_l, 't': tipo}