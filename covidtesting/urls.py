
from django.contrib import admin
from django.urls import path
from .views import home_page, details_page, validate_details, about, graph

urlpatterns = [
    path("home/", home_page, name="home"),
    path("details/", details_page, name="details_page"),
    path("results", validate_details, name="results"),
    path("about/", about, name="about"),
    path("graph/", graph, name="graph"),
]
