from django.db import models
from ckeditor.fields import RichTextField


class BaseVehicle(models.Model):
    name = models.CharField(max_length=128)
    age = models.PositiveIntegerField(help_text="The age of the vehicle in years")
    registration_nr = models.CharField(max_length=128)
    max_passengers = models.PositiveIntegerField(help_text="The amount of passengers this vehicle can transport")
    description = RichTextField(max_length=2048, blank=True, null=True)
    available = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class AirPlane(BaseVehicle):
    wing_span = models.PositiveIntegerField(help_text="The wing span of the plane in meters")
    requires_copilot = models.BooleanField()


class Boat(BaseVehicle):
    depth = models.PositiveIntegerField(help_text="The depth of the boat in meters")
    type = models.CharField(choices=(("sail_yacht", "Sailing yacht"), ("luxery_yacht", "Delux yacht"), ("cruise_ship", "Cruise ship")), max_length=32)


class LandVehicle(BaseVehicle):
    nr_wheels = models.PositiveIntegerField()
    electric = models.BooleanField()