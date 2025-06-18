import uuid
from datetime import timedelta

from django.db import models
from utils.choices import AuditFields


class Artist(AuditFields):
    object_id = models.UUIDField(
        unique=True,
        null=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name="Public identifier",
    )
    artist_uid = models.CharField(max_length=256, null=True, blank=True, verbose_name="Artist UID")
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="artist_profile/", null=True, blank=True)
    created_by = models.PositiveIntegerField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
