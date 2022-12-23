from django.contrib import admin

from .models import (
    Advertiser,
    Campaign,
    AdvertisementGroup,
    Advertisement,
    AdvertisementGroupTargetingRule
)

# Register your models here.

class AdvertisementInline(admin.StackedInline):
    model = Advertisement
    fk_name = 'advertisement_group'

class AdvertisementGroupTargetingRuleInline(admin.StackedInline):
    model = AdvertisementGroupTargetingRule
    fk_name = 'advertisement_group'

class AdvertisementGroupAdmin(admin.ModelAdmin):
    inlines = [AdvertisementInline, AdvertisementGroupTargetingRuleInline]

admin.site.register(Advertiser)
admin.site.register(Campaign)
admin.site.register(AdvertisementGroup, AdvertisementGroupAdmin)