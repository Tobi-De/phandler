from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Patient, Record


@receiver(post_save, sender=Patient)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Record.objects.create(patient=instance)
