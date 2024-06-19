from django import forms
from street_seeker.models import Reservation  

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date', 'reservation_time', 'guests']
