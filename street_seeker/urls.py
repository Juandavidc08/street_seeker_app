from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("street_search/", views.places, name="street_search"),
]