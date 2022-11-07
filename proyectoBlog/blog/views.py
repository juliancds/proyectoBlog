from django.shortcuts import render
from blog.models import modelBlog
from blog.forms import modelBlogForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.


def mostrar_inicio(request):
    articulos = modelBlog.object.all()
    contexto = {"articulos": articulos}
    return render(request, "blog/inicio.html", contexto)


class ArticulosList(ListView):
    model = modelBlog
    template_name = "blog/articulos.html"


class ArticuloDetalle(DetailView):
    model = modelBlog
    template_name = "blog/articulo_detalle.html"


class ArticuloEditar(UpdateView):
    model = modelBlog
    success_url = "/blog/mis_articulos"
    fields = ["titulo", "subtitulo", "seccion", "contenido", "autor", "fecha"]


class ArticuloBorrar(DeleteView):
    model = modelBlog
    success_url = "/blog/mis_articulos"


def crear_articulo(request):
    if request.method != "POST":
        mi_articulo = modelBlogForm()
    else:
        mi_articulo = modelBlogForm(request.POST)
        if mi_articulo.is_valid():
            informacion = mi_articulo.cleaned_data
            articulo = modelBlog(
                titulo=informacion["titulo"],
                subtitulo=informacion["subtitulo"],
                seccion=informacion["seccion"],
                contenido=informacion["contenido"],
                autor=informacion["autor"],
                fecha=informacion["fecha"],
            )
            articulo.save()
            return render(request, "blog/inicio.html")

    contexto = {"articulo": mi_articulo}

    return render(request, "blog/crear_articulo.html", contexto)
