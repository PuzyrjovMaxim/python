from django.contrib import admin

# Register your models here.

from .models import Satellite, Planet, Galaxy

#admin.site.register(Order)
#admin.site.register(Buyer)
#admin.site.register(Car)

# Define the admin class
class SatelliteAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    list_filter = ('name', 'age')

admin.site.register(Satellite, SatelliteAdmin)


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'satellite')
    list_filter = ('name', 'age', 'satellite')

# Register the Admin classes for Car using the decorator

@admin.register(Galaxy)
class GalaxyAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'planet')
    list_filter = ('name', 'age', 'planet')