from django.conf.urls import patterns, url
from GraphSearchApp import views

urlpatterns = patterns('',
    url(r'^login/', 'views.login', name='login'),
    url(r'^$', 'views.main', name='main'),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': 'static/assets/favicon.ico'}),
)