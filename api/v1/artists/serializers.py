from api.v1.general.serializers import (
    AchievementsSerializer,
    EducationSerializer,
    QualificationSerializer,
)
from book_now.models import Artist
from rest_framework import serializers


class ArtistSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True, required=False)
    qualifications = QualificationSerializer(many=True, required=False)
    achievements = AchievementsSerializer(many=True, required=False)

    class Meta:
        model = Artist
        fields = "__all__"
