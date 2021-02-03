from django.db import models

# Create your models here.
class Location(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    satellite = models.BooleanField(default=False)
    shipid = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        unique_together = ['lat', 'long']


