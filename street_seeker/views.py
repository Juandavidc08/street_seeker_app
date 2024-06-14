from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Place, Reservation
from .forms import ReservationForm, SignupForm
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

@login_required
def place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    form = ReservationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        reservation = form.save(commit=False)
        reservation.user = request.user  # Assign the current logged-in user to the reservation
        reservation.place = place
        reservation.save()
        return redirect('reservation_confirmation')  # Redirect to a confirmation page or home page after booking

    context = {
        'place': place,
        'form': form,
    }
    return render(request, 'place_details.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
