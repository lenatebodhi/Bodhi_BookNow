from book_now.models import Booking
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Booking)
def booking_code_created(sender, instance, created, **kwargs):
    if created:
        booking_id = f"BK-{instance.id}"
        instance.booking_uid = booking_id
        instance.save()
