# api/v1/tours/serializers.py

from rest_framework import serializers
from book_now.models import Tours  # Adjust the import path
from api.v1.artists.serializers import ArtistSerializer  # Reuse existing artist serializer


class TourSerializer(serializers.ModelSerializer):
    host = ArtistSerializer(read_only=True)
    crew = ArtistSerializer(many=True, read_only=True)

    class Meta:
        model = Tours
        fields = [
            "object_id",
            "tour_uid",
            "name",
            "image",
            "description",
            "duration_min",
            "duration_max",
            "host",
            "crew",
            "created_by",
            "is_active",
        ]
