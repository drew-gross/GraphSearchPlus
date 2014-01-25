from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^facebook/', include('django_facebook.urls')),
	url(r'^accounts/', include('django_facebook.auth_urls')),
	
    url(r'^login/', 'GraphSearchApp.views.login', name='login'),
    url(r'^turkerview/', 'GraphSearchApp.views.turkerview', name='turkerview'),
    url(r'^/?$', 'GraphSearchApp.views.main', name='main'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='static/assets/favicon.ico')),
)
