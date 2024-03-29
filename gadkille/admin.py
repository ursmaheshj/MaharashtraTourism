from django.contrib import admin
from import_export.admin import ImportExportMixin

from gadkille.models import AboutBackground, AboutUs, Activity, BestClick, ContactBackground, CustomerContact, Destination, DestinationBackground, Feedback, Gallery, GalleryBackground, HomeBackground, TeamMember, TrekPhoto, UpcomingTreks

class ExportContact(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'mobile', 'subject', 'message']


# Register your models here.
admin.site.register(HomeBackground)
admin.site.register(UpcomingTreks)
admin.site.register(BestClick)
admin.site.register(Activity)
admin.site.register(Feedback)

admin.site.register(AboutBackground)
admin.site.register(AboutUs)
admin.site.register(TeamMember)

admin.site.register(DestinationBackground)
admin.site.register(Destination)

admin.site.register(GalleryBackground)
admin.site.register(TrekPhoto)
admin.site.register(Gallery)

admin.site.register(ContactBackground)
admin.site.register(CustomerContact,ExportContact)