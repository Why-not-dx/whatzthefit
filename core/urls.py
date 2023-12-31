from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_user, name="logout"),
    path("account/", views.account, name="account"),
    path("abouts/", views.abouts, name="abouts"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm), name="login"),
]

# here the login path is using a built in django login view that we access in contrib.auth.
# imported it as auth_views so it doesn't conflict with the views import from this folder