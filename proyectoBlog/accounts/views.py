from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from accounts.forms import AvatarForm, UserEditionForm
from accounts.models import Avatar

# Create your views here.


# def login_request(request):
# if request.method == "GET":
# form = AuthenticationForm()
# return render(request, "accounts/login.html", {"form": form})
# form = AuthenticationForm(request, data=request.POST)
# if not form.is_valid():
# return render(
#           request,
#        "blog/articulos.html",
#          {"mensaje": "Error: los datos ingresados no son correctos"},
#       )
#   else:
#       username = form.cleaned_data.get("username")
#       password = form.cleaned_data.get("password")
#       user = authenticate(username=username, password=password)
#      if user is not None:#
#            return render(
#             request, "blog/articulos.html", {"mensaje": f"Bienvenido {username}"}
#           )
#      else:
#          return render(
#               request,
#              "blog/articulos.html",
#               {"mensaje": "El usuario no existe en nuestra aplicación"},
#          )


class MyLogin(LoginView):
    template_name = "accounts/login.html"


class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "accounts/logout.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request, "blog/articulos.html", {"mensaje": username_capturado}
            )

    else:
        form = UserCreationForm()

    return render(request, "accounts/registro.html", {"form": form})


@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "blog/inicio.html")

    contexto = {"user": user, "form": form, "avatar": avatar.imagen.url}
    return render(request, "blog/inicio.html", {"avatar": avatar.imagen.url})


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "blog/inicio.html")

    contexto = {"form": form}
    return render(request, "accounts/avatar_form.html", contexto)
