from django.contrib import admin
from .models import Mobiles, Manufacturer, Brand


@admin.register(Mobiles)
class MobilesAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Mobiles._meta.get_fields()]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "nationality"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass
