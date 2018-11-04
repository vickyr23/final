from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listado),
    url(r'^detalle/(?P<pk>[0-9]+)/$', views.detalle, name='detalle'),
]
