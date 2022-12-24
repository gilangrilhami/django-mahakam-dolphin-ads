from tqdm import tqdm

from django.core.management import BaseCommand

from advertisements.models import Advertisement

from dashboard.models import DenormalizedAdvertisement

class Command(BaseCommand):
    """
    This command is used to create denormalized advertisements from the existing advertisements in the database.

    """

    help = 'Creates denormalized advertisements from existing advertisements'

    def handle(self, *args, **options):
        """
        Query all advertisements and their related advertisement group and campaign. 
        Pre-fetch the targeting rules and slots for each advertisement group.

        For each advertisement, retrieve the advertisement group, campaign, site, 
        slot, and tags from the targeting rules. 

        Create a denormalized advertisement for each combination of site and slot and 
        append it to a list. 

        Use tqdm to display a progress bar and update it for each advertisement 
        processed. 

        After processing all advertisements, use bulk_create to create all 
        denormalized advertisements in a single query.
        
        :param self: Access variables that belongs to the class
        :param *args: Allow for an arbitrary number of arguments to be passed in
        :param **options: Pass arguments to the command
        :return: None

        :doc-author: gilangrilhami
        """
        # Query all advertisements
        advertisements = Advertisement.objects.select_related(
            'advertisement_group', 'advertisement_group__campaign'
        ).prefetch_related(
            'advertisement_group__targeting_rules__slot'
        )

        denormalized_advertisements = []

        # Use tqdm to display a progress bar
        with tqdm(total=advertisements.count()) as pbar:
            for advertisement in advertisements:
                # Get the advertisement group and campaign for the advertisement
                advertisement_group = advertisement.advertisement_group
                campaign = advertisement_group.campaign

                # Get the site and slot for the advertisement group's targeting rules
                targeting_rules = advertisement_group.targeting_rules.all()
                sites = [slot.site for tr in targeting_rules for slot in tr.slot.all()]
                slots = [slot for tr in targeting_rules for slot in tr.slot.all()]

                # Get the tags for the advertisement group's targeting rules
                tags = ','.join([tr.tags for tr in targeting_rules])

                # Create a denormalized advertisement for each site and slot
                for site, slot in zip(sites, slots):
                    denormalized_advertisements.append(DenormalizedAdvertisement(
                        advertisement=advertisement.guid,
                        group=advertisement_group.guid,
                        campaign=campaign.guid,
                        site=site.guid,
                        slot=slot.guid,
                        tags=tags,
                        data=advertisement.data
                    ))

                # Increment the progress bar
                pbar.update(1)

        # Use bulk_create to create all denormalized advertisements in a single query
        DenormalizedAdvertisement.objects.bulk_create(denormalized_advertisements)
