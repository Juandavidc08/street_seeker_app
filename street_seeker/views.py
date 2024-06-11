from django.shortcuts import render
from django.http import HttpResponse
from .models import Place

# Create your views here.

def home(request):
    return render(request, "home.html")


def places(request):
    venue = Place.objects.all()
    return render(request, "street_search.html", {"places": venue})