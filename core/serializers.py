from rest_framework import serializers
from core.models import Location
# Serializers define the API representation.



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "lat", "long", "satellite", "shipid"]

