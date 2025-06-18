from book_now.models import Event  # Adjust import if needed
from rest_framework import serializers
from api.v1.artists.serializers import ArtistSerializer


class EventSerializer(serializers.ModelSerializer):
    host = ArtistSerializer(read_only=True)
    crew = ArtistSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            "object_id",
            "event_uid",
            "name",
            "image",
            "short_description",
            "description",
            "duration_min",
            "duration_max",
            "host",
            "crew",
            "created_by",
            "is_active",
        ]
