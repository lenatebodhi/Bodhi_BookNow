from django.db import models
from utils.choices import AuditFields

class Occasion(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
