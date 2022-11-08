from django.urls import path

from blog.views import (
    crear_articulo,
    ArticulosList,
    ArticuloDetalle,
    ArticuloEditar,
    ArticuloBorrar,
    mostrar_inicio,
)

urlpatterns = [
    path("nuevo_articulo/", crear_articulo, name="nuevo_articulo"),
    path("mis_articulos/", ArticulosList.as_view(), name="mis_articulos"),
    path("r'(?P<pk>\d+)^$'", ArticuloDetalle.as_view(), name="mi_articulo_detalle"),
    path("editar/<pk>", ArticuloEditar.as_view(), name="mi_articulo_editar"),
    path("borrar/<pk>", ArticuloBorrar.as_view(), name="mi_articulo_borrar"),
    path("inicio", mostrar_inicio, name="Inicioblog"),
]
