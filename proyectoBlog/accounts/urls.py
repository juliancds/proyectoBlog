from django.urls import path
from accounts.views import MyLogin, MyLogout, register


urlpatterns = [
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    path("register/", register, name="Register"),
]
