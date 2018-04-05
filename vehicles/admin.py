from django.contrib import admin
from .models import LandVehicle, Boat, AirPlane


class BaseVehicleAdmin(admin.ModelAdmin):
    list_filter = ("available", )
    list_display = ("name", "available")
    pass


@admin.register(LandVehicle)
class LandVehicleAdmin(BaseVehicleAdmin):
    pass


@admin.register(Boat)
class BoatAdmin(BaseVehicleAdmin):
    pass


@admin.register(AirPlane)
class AirPlaneAdmin(BaseVehicleAdmin):
    pass
