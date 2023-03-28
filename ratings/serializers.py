from rest_framework import serializers
from ratings.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'trip', 'driver', 'comment', 'value']

    def to_representation(self, instance):
        """
        Add trip and driver details to the response.
        """
        data = super().to_representation(instance)
        data['id'] = instance.id
        data['trip'] = instance.trip
        data['driver'] = instance.driver.id
        data['comment'] = instance.driver.id
        data['value'] = instance.driver.id
        return data