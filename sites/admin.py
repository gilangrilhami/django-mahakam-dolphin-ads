from django.contrib import admin

from .models import Publisher, Site, Slot

# Register your models here.

class SlotInline(admin.StackedInline):
    model = Slot
    fk_name = 'site'

class SiteAdmin(admin.ModelAdmin):
    inlines = [SlotInline]

admin.site.register(Publisher)
admin.site.register(Site, SiteAdmin)
