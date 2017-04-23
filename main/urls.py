from django.conf.urls import url 
from . import views

urlpatterns = [
	url(
		r'^posts/(?P<slug>[-\w]+)$',
		views.DetailPost.as_view(),
		name='detail'
	),
	url(
		r'^$',
		views.Home.as_view(), name='home'
	),

]