from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name
