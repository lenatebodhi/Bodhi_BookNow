import uuid
from datetime import timedelta

from django.db import models
from utils.choices import AuditFields

from .artists import Artist


class Tours(AuditFields):
    object_id = models.UUIDField(
        unique=True,
        null=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name="Public identifier",
    )
    tour_uid = models.CharField(max_length=256, null=True, blank=True, verbose_name="Tour UID")
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="tour_thumbnails/", null=True, blank=True)

    description = models.TextField()

    duration_min = models.DurationField(help_text="Minimum duration")
    duration_max = models.DurationField(null=True, blank=True, help_text="max duration")

    host = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, related_name="hosted_tours")
    crew = models.ManyToManyField(Artist, related_name="tour_crews", blank=True)

    created_by = models.PositiveIntegerField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Tour"
        verbose_name_plural = "Tours"

    def __str__(self):
        return self.name

    def display_duration(self):
        def format_td(td):
            total_minutes = td.total_seconds() // 60
            hours = int(total_minutes // 60)
            minutes = int(total_minutes % 60)
            return f"{hours}:{minutes:02d}"

        if self.duration_max:
            return f"{format_td(self.duration_min)} - {format_td(self.duration_max)} hrs"
        return f"{format_td(self.duration_min)} hrs"
