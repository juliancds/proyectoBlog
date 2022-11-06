from django.db import models
from datetime import datetime

# Create your models here.


class modelBlog(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=70)
    subtitulo = models.CharField(max_length=280)
    seccion = models.CharField(max_length=70)
    contenido = models.CharField(max_length=1120)
    autor = models.CharField(max_length=70)
    fecha = models.DateField(default=datetime.now)
    imagen = models.ImageField(upload_to="pictures", null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} by {self.autor}"
