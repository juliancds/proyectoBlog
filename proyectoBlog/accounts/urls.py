from django.urls import path
from accounts.views import MyLogin, MyLogout, register, editar_perfil


urlpatterns = [
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    path("register/", register, name="Register"),
    path("editar_perfil/", editar_perfil, name="EditarPerfil"),
]
