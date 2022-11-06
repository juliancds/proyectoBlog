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


def inicio(request):
    pass


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
