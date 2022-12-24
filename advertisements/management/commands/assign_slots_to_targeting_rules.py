import random

from django.core.management.base import BaseCommand

from advertisements.models import AdvertisementGroupTargetingRule
from sites.models import Slot


class Command(BaseCommand):
    """
    Randomly assigns existing slots to advertisement group targeting rules.
    """

    help = 'Randomly assigns existing slots to advertisement group targeting rules'
    
    def handle(self, *args, **options):
        """
        Assigns a random slot to each advertisement group targeting rule.
        
        This function iterates over all advertisement group targeting rules 
        in the database and assigns a random slot to each rule. The changes 
        are then saved to the database.
        
        :param self: Access variables that belongs to the class
        :param *args: Allow for an arbitrary number of arguments to be passed in
        :param **options: Pass arguments to the command
        :return: None
        
        :doc-author: gilangrilhami
        """

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
