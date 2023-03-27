from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    name = serializers.CharField()
    # coordinates = serializers.DictField(
    #     child=serializers.DecimalField(max_digits=9, decimal_places=6)
    # )

    latitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6)
