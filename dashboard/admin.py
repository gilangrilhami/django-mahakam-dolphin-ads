from django.contrib import admin

from .models import DenormalizedAdvertisement

# Register your models here.

class DenormalizedAdvertisementAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # Use the 'denormalized_db' database for the queryset
        return super().get_queryset(request).using('dashboard')
        
    def has_add_permission(self, request):
        # Disable the 'Add' button in the Django admin
        return False

    def has_change_permission(self, request, obj=None):
        # Disable the 'Save' and 'Save and continue editing' buttons in the Django admin
        return False

admin.site.register(DenormalizedAdvertisement, DenormalizedAdvertisementAdmin)