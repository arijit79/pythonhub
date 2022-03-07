from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
    path("password-reset", views.pass_reset, name="pass-reset"),
    path("password-reset-confirm/", views.pass_confirm, name="pass-confirm"),
    path("profile/", views.profile, name="profile"),
]
