from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("adesunbo", views.adesunbo, name="adesunbo"),
    path("motunrade", views.motunrade, name="motunrade")
]
