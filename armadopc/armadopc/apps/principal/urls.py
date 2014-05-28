from django.conf.urls import patterns, include, url
from views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    

    url(r'^$',inicio),
    url(r'^caracteristicas$',Armadopc),   
    url(r'^logeo/',logeo),
    url(r'registro/$',registro_cliente),
	url(r'clientes/$',clientes),
   	
)    

