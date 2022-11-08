from django.shortcuts import render
from blog.models import modelBlog
from blog.forms import modelBlogForm
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from accounts.models import Avatar

# Create your views here.


def mostrar_inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}
    variable = modelBlog.objects.all()
    contexto = {"avatar": avatar.imagen.url, "llave": variable}
    return render(request, "blog/inicio.html", contexto)


class ArticulosList(LoginRequiredMixin, ListView):
    model = modelBlog
    template_name = "blog/articulos.html"


class ArticuloDetalle(DetailView):
    model = modelBlog
    template_name = "blog/articulo_detalle.html"


class ArticuloEditar(LoginRequiredMixin, UpdateView):
    model = modelBlog
    success_url = "/blog/mis_articulos"
    fields = ["titulo", "subtitulo", "seccion", "contenido", "autor", "fecha"]


class ArticuloBorrar(LoginRequiredMixin, DeleteView):
    model = modelBlog
    success_url = "/blog/mis_articulos"


@login_required()
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
