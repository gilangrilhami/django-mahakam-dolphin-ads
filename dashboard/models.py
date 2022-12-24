from django.db import models

# Create your models here.

class DenormalizedAdvertisement(models.Model):
    advertisement = models.UUIDField(blank=False, null=False, editable=False)
    group = models.UUIDField(blank=False, null=False, editable=False)
    campaign = models.UUIDField(blank=False, null=False, editable=False)
    site = models.UUIDField(blank=False, null=False, editable=False)
    slot = models.UUIDField(blank=False, null=False, editable=False)
    tags = models.TextField()
    data = models.TextField()
