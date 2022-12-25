from django_clickhouse.clickhouse_models import ClickHouseModel, ClickHouseSyncModel
from django_clickhouse.engines import MergeTree
from infi.clickhouse_orm import fields

from django.db import models

from datetime import datetime


# Create your models here.

class DenormalizedAdvertisement(ClickHouseSyncModel):
    advertisement = models.UUIDField(blank=False, null=False, editable=False)
    group = models.UUIDField(blank=False, null=False, editable=False)
    campaign = models.UUIDField(blank=False, null=False, editable=False)
    site = models.UUIDField(blank=False, null=False, editable=False)
    slot = models.UUIDField(blank=False, null=False, editable=False)
    tags = models.TextField()
    data = models.TextField()

    @classmethod
    def is_read_only(cls):
        return False

    @classmethod
    def is_system_model(cls):
        return False

    @classmethod
    def fields(cls, writable=True):
        return [
            'advertisement',
            'group',
            'campaign',
            'site',
            'slot',
            'tags',
            'data',
        ]

    @classmethod
    def has_funcs_as_defaults(cls):
        return True

    @classmethod
    def table_name(cls):
        return 'denormalized_advertisement'

    @classmethod
    def set_database(cls, database):
        cls._database = database

class ClickhouseDenormalizedAdvertisement(ClickHouseModel):
    django_model = DenormalizedAdvertisement

    advertisement = fields.UUIDField()
    group = fields.UUIDField()
    campaign = fields.UUIDField()
    site = fields.UUIDField()
    slot = fields.UUIDField()
    tags = fields.StringField()
    data = fields.StringField()
    created_at = fields.DateTimeField(default=datetime.now())

    engine = MergeTree('created_at', ('created_at',))
