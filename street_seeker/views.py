from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
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


def place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    user_authenticated = request.user.is_authenticated
    form = ReservationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        if user_authenticated:
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.place = place
            reservation.save()
            return redirect('reservation_confirmation')
        else:
            return redirect('login')  # Redirect to login page

    context = {
        'place': place,
        'form': form,
        'user_authenticated': user_authenticated,
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

class PlaceDetailView(LoginRequiredMixin, DetailView):
    model = Place
    template_name = 'place_details.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReservationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = self.request.user
            reservation.place = self.get_object()
            reservation.save()
            return redirect('reservation_confirmation')
        return self.render_to_response(self.get_context_data(form=form))
