import uuid
from django.db import models
from sites.models import Slot

# Create your models here.

class Advertiser(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

class Campaign(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE, related_name='campaigns')
    name = models.CharField(max_length=255)

class AdvertisementGroup(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='advertisement_groups')
    name = models.CharField(max_length=255)

class AdvertisementGroupTargetingRule(models.Model):
    advertisement_group = models.ForeignKey(AdvertisementGroup, on_delete=models.CASCADE, related_name='targeting_rules')
    slot = models.ManyToManyField(Slot, related_name='targeting_rules')
    tags = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Advertisement(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    advertisement_group = models.ForeignKey(AdvertisementGroup, on_delete=models.CASCADE, related_name='advertisements')
    data = models.TextField()