import random

from django.core.management.base import BaseCommand

from advertisements.models import AdvertisementGroupTargetingRule
from sites.models import Slot


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Query all advertisement group targeting rules
        targeting_rules = AdvertisementGroupTargetingRule.objects.all()

        # Query all slots
        slots = Slot.objects.all()

        # Iterate over the targeting rules
        for targeting_rule in targeting_rules:
            # Select a random slot
            random_slot = random.choice(slots)
            # Add the slot to the targeting rule
            targeting_rule.slot.add(random_slot)
            # Save the changes to the database
            targeting_rule.save()

        self.stdout.write(self.style.SUCCESS('Successfully assigned slots to targeting rules'))
