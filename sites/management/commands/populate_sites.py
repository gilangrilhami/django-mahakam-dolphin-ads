from faker import Faker
from django.core.management import BaseCommand

from sites.models (
    Site,
    Slot,
    Publisher,
)
fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):

        # Create publishers
        publishers = []
        for i in range(10):
            publisher = Publisher.objects.create(name=fake.company())
            publishers.append(publisher)

        # Create sites for each publisher
        for publisher in publishers:
            for i in range(3):
                site = Site.objects.create(publisher=publisher, name=fake.company())

                # Create slots for each site
                for i in range(10):
                    Slot.objects.create(site=site, name=fake.word())
