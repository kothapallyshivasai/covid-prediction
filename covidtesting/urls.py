
from django.contrib import admin
from django.urls import path
from .views import home_page, details_page, location_bar_chart, validate_details, about, graph

urlpatterns = [
    path("home/", home_page, name="home"),
    path("details/", details_page, name="details_page"),
    path("results", validate_details, name="results"),
    path("about/", about, name="about"),
    path("graph/", graph, name="graph"),
    path("location-graph/", location_bar_chart, name="location_bar_chart"),
]
