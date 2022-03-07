from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>", views.answer, name="challenge-answer"),
    path("previous/<int:pk>", views.last_challenge, name="last-challenge")
]
