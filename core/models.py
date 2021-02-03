from django.db import models

# Create your models here.
class Location(models.Model):
    lat = models.FloatField()
    long = models.FloatField()

    class Meta:
        unique_together = ['lat', 'long']


