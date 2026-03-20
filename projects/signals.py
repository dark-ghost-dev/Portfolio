import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Project
from .services.og_image_processing import process_og_image


@receiver(post_save, sender=Project)
def procesar_og_image(sender, instance, created, **kwargs):
    if not instance.og_image:
        return

    # Evitar loops infinitos
    if getattr(instance, "_processing", False):
        return

    instance._processing = True

    old_image = None

    if not created:
        try:
            old = Project.objects.get(pk=instance.pk)
            old_image = old.og_image
        except Project.DoesNotExist:
            pass

    # Procesar imagen
    content_file = process_og_image(instance.og_image)

    filename = f"{slugify(instance.title)}.jpg"

    instance.og_image.save(filename, content_file, save=False)

    # Guardar sin volver a disparar lógica innecesaria
    instance.save(update_fields=['og_image'])

    # Eliminar imagen anterior
    if old_image and old_image != instance.og_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)

    instance._processing = False