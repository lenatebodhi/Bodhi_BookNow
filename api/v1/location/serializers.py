from rest_framework import serializers
from book_now.models import Booking, Location, Occasion


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
