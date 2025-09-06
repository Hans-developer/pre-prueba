from django.db import models

# Create your models here.

class Peliculas(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes/')
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.titulo
    


