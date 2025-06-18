from book_now.models import Artist
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Artist)
def artist_code_created(sender, instance, created, **kwargs):
    if created:
        artist_id = f"ART-{instance.id}"
        instance.artist_uid = artist_id
        instance.save()
