"""Ejercicio1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

from Ejemplo1App import views
#import Ejemplo1App.views  /tambien se puede pero en vez de usar views.index se usa Ejemplo1App.views.index
#para redirecionar se necesita importar redirect y se usa return redirect('www.pagina.com')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index, name="index"),
    path('',views.index, name="index"), #Cuando el primer paramaetro esta vacio se declara como la pagina principal, mientra no este vacio es enobre es el url al que se peude ir
    path('producto', views.producto, name='producto'),
    path('cita_rapida', views.cita_rapida, name= 'cita_rapida'),
    path('sesion',views.sesion , name= 'sesion'),
    path('registro',views.registro, name='registro'),
    path('save_citaR',views.save_citaR,name= 'save_citaR'),
    path('indexUser',views.indexUser, name='indexUser')
]


#configuracion para cargar imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)