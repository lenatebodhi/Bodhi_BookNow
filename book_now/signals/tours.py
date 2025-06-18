from book_now.models import Tours
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Tours)
def tour_code_created(sender, instance, created, **kwargs):
    if created:
        tour_id = f"TR-{instance.id}"
        instance.tour_uid = tour_id
        instance.save()
