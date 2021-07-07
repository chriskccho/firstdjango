from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chris", views.chris, name="chris"),
    path("<str:name>", views.greet, name="greet")
]