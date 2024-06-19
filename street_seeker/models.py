from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name
        
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.place.name} - {self.reservation_date}"


