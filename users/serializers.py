from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    passenger = serializers.SerializerMethodField()

    class Meta:
        model = User
        # NOTE: Add more fields as needed in the JSON response
        fields = ("id", "email", "first_name", "last_name", "photo", "passenger")

    def get_passenger(self, obj):
        return {
            "routines": obj.passenger.routines.all(),
            # add more passenger fields as needed
        }
