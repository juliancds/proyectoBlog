from django.urls import path

from blog.views import crear_articulo

urlpatterns = [
    path("nuevo_articulo/", crear_articulo, name="nuevo_articulo"),
]
