from django_clickhouse.clickhouse_models import ClickHouseModel
from django_clickhouse.engines import MergeTree
from infi.clickhouse_orm import fields

from django.db import models

from datetime import datetime


# Create your models here.

class DenormalizedAdvertisement(models.Model):
    advertisement = models.UUIDField(blank=False, null=False, editable=False)
    group = models.UUIDField(blank=False, null=False, editable=False)
    campaign = models.UUIDField(blank=False, null=False, editable=False)
    site = models.UUIDField(blank=False, null=False, editable=False)
    slot = models.UUIDField(blank=False, null=False, editable=False)
    tags = models.TextField()
    data = models.TextField()

class ClickhouseDenormalizedAdvertisement(ClickHouseModel):
    advertisement = fields.UUIDField()
    group = fields.UUIDField()
    campaign = fields.UUIDField()
    site = fields.UUIDField()
    slot = fields.UUIDField()
    tags = models.TextField()
    data = models.TextField()
    created_at = fields.DateTimeField(default=datetime.now())

    engine = MergeTree('created_at', ('created_at',))
