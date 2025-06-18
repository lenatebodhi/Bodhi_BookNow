import uuid

from django.db import models
from utils.choices import AuditFields

from .artists import Artist
from .events import Event
from .location import Location
from .occations import Occasion


class Booking(AuditFields):
    object_id = models.UUIDField(
        unique=True,
        null=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name="Public identifier",
    )
    booking_uid = models.CharField(max_length=256, null=True, blank=True, verbose_name="Booking UID")
    user_id = models.PositiveIntegerField()  # Coming from JWT
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True, related_name="booking_event")
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True, related_name="booking_artist")
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True, related_name="booking_location"
    )
    occations = models.ManyToManyField(
        Occasion,
        related_name="booking_occations",
        blank=True,
        verbose_name="Occasions",
    )
    additional_info = models.TextField(null=True, blank=True)
    estimate_inr = models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"{self.booking_uid}"
