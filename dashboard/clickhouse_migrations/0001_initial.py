from django_clickhouse import migrations
from dashboard.models import ClickhouseDenormalizedAdvertisement

class Migration(migrations.Migration):
    operations = [
        migrations.CreateTable(ClickhouseDenormalizedAdvertisement)
    ]