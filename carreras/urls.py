from django.conf.urls import url
from . import views

urlpatterns = [
	url(
		r'^(?P<nombre>[-\w]+)/$',
		views.DetailCarrera.as_view(),
		name='detalle'
	),
]