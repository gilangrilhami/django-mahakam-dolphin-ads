from django.db import models

from sites.models import Site, Slot
from advertisements.models import Advertisement, AdvertisementGroup, Campaign

# Create your models here.

class DenormalizedAdvertisement(models.Model):
    advertisement = models.OneToOneField(Advertisement, on_delete=models.CASCADE, primary_key=True)
    group = models.OneToOneField(AdvertisementGroup, on_delete=models.CASCADE)
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE)
    tags = models.TextField()
    data = models.TextField()

    def save(self, *args, **kwargs):
     return

    def delete(self, *args, **kwargs):
        return