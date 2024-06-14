from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from random import sample

# Create your views here.

def home(request):
    return render(request, "home.html")

def places(request):
    all_places = list(Place.objects.all())
    if len(all_places) >= 3:
        selected_places = sample(all_places, 3)
    else:
        selected_places = all_places
    return render(request, "street_search.html", {"places": selected_places})