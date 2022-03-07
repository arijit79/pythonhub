from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.chapter_index, name="chapter_index"),
    path("<int:pk>/<int:s_no>/", views.chapter, name="chapter"),
    path("article", views.article, name="article")
]
