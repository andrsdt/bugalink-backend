from rest_framework import serializers

from driver_routines.models import DriverRoutine
from driver_routines.serializers import DriverRoutineSerializer
from drivers.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    routines = DriverRoutineSerializer(many=True)

    class Meta:
        model = Driver
        fields = ["id", "routines"]

    # TODO: check if necessary, maybe the user is not being created with this
    # Used internally for creating a driver
    # def create(self, validated_data):
    #     routines_data = validated_data.pop("routines")
    #     driver = Driver.objects.create(**validated_data)
    #     for routine_data in routines_data:
    #         DriverRoutine.objects.create(driver=driver, **routine_data)

    #     # Link routines to the driver
    #     driver.routines.set(routines_data)

    #     return driver
