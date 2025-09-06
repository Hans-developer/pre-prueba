from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Peliculas
# Create your views here.



def home(request):
    return render(request, 'repelis/index.html')


def pelicula(request):
    pelis = Peliculas.objects.all()
    return render(request, 'repelis/peliculas.html', {'pelis': pelis})


def detalle(request, id):
    pelicula = get_object_or_404(Peliculas, id=id)
    return render(request, 'repelis/detalle.html', {'pelicula': pelicula})


def contacto(request):
    return render(request, 'repelis/contacto.html')

def acerca(request):
    return render(request, 'repelis/acerca.html')

def libre(request):
    return render(request, 'repelis/libre.html')




