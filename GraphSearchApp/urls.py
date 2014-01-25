from django.conf.urls import patterns, url
from GraphSearchApp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')
)