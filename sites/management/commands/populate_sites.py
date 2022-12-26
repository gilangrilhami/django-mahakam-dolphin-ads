from faker import Faker
from django.core.management import BaseCommand

from sites.models import (
    Site,
    Slot,
    Publisher,
)
fake = Faker()

class Command(BaseCommand):
    """
    Django command to create publishers, sites, and slots for testing purposes.
    """

    help = 'Create publishers, sites, and slots for testing purposes'

    def handle(self, *args, **options):
        """
        Create publishers, sites, and slots.
        
        This method creates 10 publishers, each with 3 sites and 10 slots.

        :param self: Access variables that belongs to the class
        :param *args: Allow for an arbitrary number of arguments to be passed in
        :param **options: Pass arguments to the command
        :return: None

        :doc-author: giangrilhami
        """

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
