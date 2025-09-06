from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('detalles/<int:id>', views.detalle, name='detalle'),
    path('pelicula/', views.pelicula, name='pelicula'),
    path('contacto/', views.contacto, name='contacto'),
    path('acerca/', views.acerca, name='acerca'),
    path('planes/', views.libre, name='planes'),
]