from rest_framework import serializers
from .models import AirPlane, LandVehicle, Boat


class AirPlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirPlane
        fields = ('id',
                  'name',
                  'age',
                  'wing_span',
                  'requires_copilot',
                  'registration_nr',
                  'registration_nr',
                  'description',
                  'available')


class LandVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandVehicle
        fields = ('id',
                  'name',
                  'age',
                  'nr_wheels',
                  'electric',
                  'registration_nr',
                  'registration_nr',
                  'description',
                  'available')


class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = ('id',
                  'name',
                  'age',
                  'depth',
                  'type',
                  'registration_nr',
                  'registration_nr',
                  'description',
                  'available')