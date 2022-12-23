import uuid
from django.db import models

# Create your models here.

class Publisher(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

class Site(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='sites')
    name = models.CharField(max_length=255)

class Slot(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='slots')
    name = models.CharField(max_length=255)