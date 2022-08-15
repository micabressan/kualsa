"""KualSA URL Configuration

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
from KualSA.views import CatalogoView, ContactoView, EmpresaView, InicioView, NovedadesView, PropiedadesView, RepresentantesView, ServicioView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', InicioView, name='inicio'),
    path('empresa/', EmpresaView, name='empresa'),
    path('catalogo/', CatalogoView, name='catalogo'),
    path('representante/', RepresentantesView, name='representante'),
    path('contacto/', ContactoView, name='contacto'),
    path('novedades/', NovedadesView, name='novedades'),
    path('propiedades/', PropiedadesView, name='propiedades'),
    path('servicio/', ServicioView, name='servicio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)