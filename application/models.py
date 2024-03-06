from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_queryset():
        return News.objects.order_by("-created_at")


class Video(models.Model):
    description = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    video = models.FileField(upload_to='videos/%Y/%m/%d/', verbose_name="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    @staticmethod
    def get_queryset():
        return Video.objects.order_by("-created_at")


@receiver(pre_delete, sender=Video)
def delete_file_on_model_delete(sender, instance, **kwargs):
    # Delete the file associated with the instance
    print("Pre-delete hook is invoked")
    instance.thumbnail.delete(False)
    instance.video.delete(False)
