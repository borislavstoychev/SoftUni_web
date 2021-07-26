from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

from templates_advanced.pythons_app.models import Python

UserModel = get_user_model()


@receiver(pre_save, sender=Python)
def delete_file_on_change_extension(sender, instance, **kwargs):

    if instance.pk:
        try:
            old_avatar = Python.objects.get(pk=instance.pk).image
        except Python.DoesNotExist:
            return
        else:
            new_avatar = instance.image
            if old_avatar and old_avatar.url != new_avatar.url:
                old_avatar.delete(save=False)
