from django.db import models
from django.contrib.auth.models import User
from street_seeker.models import Reservation as StreetSeekerReservation

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='your_plans_reservations')
    # Import Place model from street_seeker app directly
    place = models.ForeignKey('street_seeker.Place', on_delete=models.CASCADE, related_name='your_plans_reservations')
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.place.name} - {self.reservation_date}"