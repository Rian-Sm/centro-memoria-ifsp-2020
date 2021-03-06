"""centro_memoria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('centro_memoria.instituicao.urls', namespace='instituicao')),
    path('admin/', admin.site.urls),
    path('galeria/', include('centro_memoria.galeria_diretores.urls', namespace='galeria')),
    path('noticias/', include('centro_memoria.noticias.urls', namespace='noticias')),
    path('eventos/', include('centro_memoria.eventos.urls', namespace='eventos')),
    path('linha-tempo/', include('centro_memoria.linha_tempo.urls', namespace='linha_tempo')),
    path('acervo/', include('centro_memoria.acervo.urls', namespace='acervo'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)