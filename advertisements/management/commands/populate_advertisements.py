import random
from faker import Faker
from django.core.management import BaseCommand

from sites.models import Slot

from advertisements.models import (
    Advertiser,
    Campaign,
    AdvertisementGroup,
    Advertisement,
    AdvertisementGroupTargetingRule
)

fake = Faker()

class Command(BaseCommand):

    """
    Populates the database with fake data for testing purposes.

    This command creates 10 advertisers, with each advertiser having 5 campaigns.
    Each campaign has 4 advertisement groups, and each advertisement group has 2 targeting rules.
    Each targeting rule is associated with a random number of slots, and each advertisement group has 10 advertisements.
    """

    help = 'Populates the database with fake data for testing purposes'

    def handle(self, *args, **options):
        """
        This function generates dummy data for the advertisements app. It does so 
        by creating advertisers, campaigns, advertisement groups, targeting rules, 
        and advertisements.
        
        Advertisers, campaigns, advertisement groups, and targeting rules are created 
        in a nested fashion, with advertisers containing campaigns, campaigns containing 
        advertisement groups, and advertisement groups containing targeting rules.
        
        Each advertisement group also contains a number of advertisements. The number of 
        advertisers, campaigns, advertisement groups, and targeting rules created, as 
        well as the number of advertisements per advertisement group, is hardcoded and 
        set to 10, 5, 4, and 2, respectively.

        The function also randomly selects a number of slots to associate with each 
        targeting rule, using the random module.

        :param self: Access variables that belongs to the class
        :param *args: Allow for an arbitrary number of arguments to be passed in
        :param **options: Pass arguments to the command
        :return: None

        :doc-author: gilangrilhami
        """

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
