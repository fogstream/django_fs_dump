from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


UPLOAD_DIR_NAME = 'fs_dump'


class Dump(models.Model):
    """
    """

    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    database_dump = models.FileField(verbose_name='database dump', upload_to=UPLOAD_DIR_NAME)
    media_dump = models.FileField(verbose_name='media dump', upload_to=UPLOAD_DIR_NAME)
    output = models.TextField(verbose_name='output')

    class Meta:
        verbose_name = 'dump'
        verbose_name_plural = 'dumps'

    def __str__(self):
        return f'Dump #{self.id} from {self.created_at:%d.%m.%Y %H:%M}'


@receiver(post_delete, sender=Dump)
def submission_delete(sender, instance, **kwargs):
    instance.database_dump.delete(False)
    instance.media_dump.delete(False)
