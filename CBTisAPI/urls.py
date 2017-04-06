from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from main import urls as MainUrls
from carreras import urls as CarrerasUrls 

urlpatterns = [
  url(
    r'^carreras/',
    include(CarrerasUrls, namespace='carreras')
  ),
	url(
		r'^',
		include(MainUrls, namespace='main')
	),
  url(r'^admin/', admin.site.urls),
  url(
    r'^media/(?P<path>.*)$',
    serve,
    {'document_root':settings.MEDIA_ROOT}
  ),

]
