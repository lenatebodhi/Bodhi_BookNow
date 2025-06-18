import re

from book_now.models import *
from rest_framework import serializers


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = "__all__"


class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = "__all__"
