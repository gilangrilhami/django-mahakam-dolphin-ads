import random
from faker import Faker
from django.core.management import BaseCommand

from advertisements.models import (
    Advertiser,
    Campaign,
    AdvertisementGroup,
    Advertisement,
    AdvertisementGroupTargetingRule
)

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):

        # Create advertisers
        advertisers = []
        for i in range(10):
            advertiser = Advertiser.objects.create(name=fake.company())
            advertisers.append(advertiser)

        # Create campaigns for each advertiser
        for advertiser in advertisers:
            for i in range(5):
                campaign = Campaign.objects.create(advertiser=advertiser, name=fake.word())

                # Create advertisement groups for each campaign
                for i in range(4):
                    advertisement_group = AdvertisementGroup.objects.create(campaign=campaign, name=fake.word())

                    # Create targeting rules for each advertisement group
                    for i in range(2):
                        targeting_rule = AdvertisementGroupTargetingRule.objects.create(
                            advertisement_group=advertisement_group,
                            tags=fake.word(),
                            description=fake.sentence()
                        )

                        # Randomly select a number of slots to associate with the targeting rule
                        num_slots = random.randint(1, 10)
                        slots = random.sample(list(Slot.objects.all()), num_slots)
                        targeting_rule.slot.set(slots)

                    # Create advertisements for each advertisement group
                    for i in range(10):
                        Advertisement.objects.create(
                            advertisement_group=advertisement_group,
                            data=fake.text()
                        )
