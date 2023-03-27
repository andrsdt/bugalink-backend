from rest_framework import serializers

from driver_routines.models import DriverRoutine
from locations.models import Location
from locations.serializers import LocationSerializer


class DriverRoutineSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    origin = LocationSerializer()
    destination = LocationSerializer()
    days_of_week = serializers.ListField(child=serializers.CharField())
    departure_time_start = serializers.DateTimeField()
    departure_time_end = serializers.DateTimeField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    note = serializers.CharField()
    is_single_ride = serializers.BooleanField()
    available_seats = serializers.IntegerField(min_value=1, max_value=8)

    def create(self, validated_data):
        origin_data = validated_data.pop("origin")
        destination_data = validated_data.pop("destination")
        # TODO: try to bring existing location if it exists
        origin = Location.objects.create(**origin_data)
        destination = Location.objects.create(**destination_data)
        return DriverRoutine.objects.create(
            origin=origin, destination=destination, **validated_data
        )
