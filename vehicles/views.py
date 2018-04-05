from django.shortcuts import render
from rest_framework import viewsets
from .models import LandVehicle, Boat, AirPlane
from .serializers import LandVehicleSerializer, BoatSerializer, AirPlaneSerializer


class AirPlaneView(viewsets.ReadOnlyModelViewSet):
    queryset = AirPlane.objects.filter(available=True)
    serializer_class = AirPlaneSerializer


class BoatView(viewsets.ReadOnlyModelViewSet):
    queryset = Boat.objects.filter(available=True)
    serializer_class = BoatSerializer


class LandVehicleView(viewsets.ReadOnlyModelViewSet):
    queryset = LandVehicle.objects.filter(available=True)
    serializer_class = LandVehicleSerializer


