from rest_framework import serializers
from book_now.models import Occasion


class OccasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occasion
        fields = ["id", "name"]
