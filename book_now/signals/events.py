from book_now.models import Event
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Event)
def event_code_created(sender, instance, created, **kwargs):
    if created:
        event_id = f"EVT-{instance.id}"
        instance.event_uid = event_id
        instance.save()
