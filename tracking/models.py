from django.db import models

# Create your models here.
PLATFORM_TYPE = (
    ('wap', 'wap'),
    ('web', 'web'),
    ('app', 'app'),
)


class PlayHub(models.Model):
    user_info = models.CharField(max_length=100, null=True, blank=True)
    time_stamp = models.DateTimeField(null=True, blank=True)
    platform_type = models.CharField(max_length=5, choices=PLATFORM_TYPE)
    # end_time = models.DateTimeField(null=True, blank=True)
    action = models.TextField(null=True, blank=True)
    add_id = models.CharField(max_length=265, null=True, blank=True)
    # tracking_device = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ["-created"]
        # verbose_name_plural = "LCs"

    def __str__(self):
        return self.user_info
