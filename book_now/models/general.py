import uuid
from datetime import timedelta

from django.db import models
from utils.choices import AuditFields

from .artists import Artist


class Education(AuditFields):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="educations")
    college = models.CharField(max_length=256)
    degree = models.CharField(max_length=256)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Education"

    def __str__(self):
        return str(self.college)


class Qualification(AuditFields):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="qualifications")
    college = models.CharField(max_length=256)
    degree = models.CharField(max_length=256)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Qualification"

    def __str__(self):
        return str(self.college)


class Achievements(AuditFields):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="achievements")
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Achievements"

    def __str__(self):
        return str(self.title)
