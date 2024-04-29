"""
URL configuration for votantes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from candidatos import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar_candidato', views.CrearCandidatosView.as_view(), name='reg_candidato'),
    path('listaC/', views.lista_candidatos, name='lista_candidatos'),
    path('eliminar/<int:id>', views.eliminar_candidato, name='eliminar_candidato'),
    path('editar_candidato/<str:pk>', views.EditarCandidatoView.as_view(), name='editar_candidato'),
    path('listaP/', views.ListaPartido.as_view(), name='lista_partidos'),
    path('eliminarP/<int:id>', views.eliminar_partido, name='eliminar_partido'),
    path('editar_partido /<str:pk>', views.EditarPartidoView.as_view(), name='editar_partido'),
    path('registrar_partido', views.CrearPartidoView.as_view(), name='reg_partido'),
    path('votaciones/', views.votaciones, name='votaciones'),
    path('votar/<int:id>', views.votar_candidato, name='votar_candidato'),
    path('listaCandidatosP/', views.lista_candidatos_puntuacion, name='lista_candidatos_puntuacion'),
    path('grafica/',views.Grafica.as_view(), name='votos_Grafica'),
    path('',views.homepage, name = 'home'),
]

