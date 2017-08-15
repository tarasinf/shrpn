from django.contrib import admin

from smartmap.forms import LocationForm
from smartmap.models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'lat', 'lng', 'address', 'created']
    form = LocationForm


admin.site.register(Location, LocationAdmin)
