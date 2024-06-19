from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation
from django.forms.widgets import DateInput, TimeInput


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date', 'reservation_time', 'guests']
        widgets = {
            'reservation_date': DateInput(attrs={'type': 'date'}),
            'reservation_time': TimeInput(attrs={'type': 'time'}),
        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']