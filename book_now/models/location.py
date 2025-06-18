from django.db import models
from utils.choices import AuditFields


class Location(AuditFields):
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    pin_code = models.CharField(max_length=10)
    contact_person_full_name = models.CharField(max_length=100)
    contact_person_phone_1 = models.CharField(max_length=15)
    contact_person_phone_2 = models.CharField(max_length=15, blank=True, null=True)
    contact_person_email = models.EmailField()
    additional_info = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.address_line_1}, {self.city}, {self.country}"
