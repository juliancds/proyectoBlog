from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class MyLogin(LoginView):
    template_name = "accounts/login.html"


class MyLogout(LogoutView):
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
