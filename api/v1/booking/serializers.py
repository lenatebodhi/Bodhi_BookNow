from rest_framework import serializers
from book_now.models import Booking, Occasion, Location
from api.v1.location.serializers import LocationSerializer
from api.v1.occasion.serializers import OccasionSerializer


class BookingSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Booking
        fields = [
            "object_id",
            "booking_uid",
            "user_id",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "event",
            "artist",
            "location",
            "additional_info",
            "estimate_inr",
        ]

    def create(self, validated_data):
        location_data = validated_data.pop("location", None)
        occations_data = validated_data.pop("occations", [])

        # Create or update location

        location = Location.objects.create(**location_data) if location_data else None

        # Create booking
        booking = Booking.objects.create(location=location, **validated_data)

        # Add many-to-many occasions
        booking.occations.set(occations_data)

        return booking
