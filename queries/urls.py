from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.query_index, name="query-index"),
    path("new/", views.new_query, name="query-new"),
    path("view/<int:query_id>", views.view_query, name="query-view"),
    path("update/<int:query_id>", views.update_query, name="query-update"),
    path("delete-query/<int:query_id>", views.delete_query, name="query-delete"),
]
