from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from ratings.models import Rating
from ratings.serializers import RatingSerializer


class RatingViewSet(
    LoginRequiredMixin,
    # GET, POST
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return RatingSerializer  # TODO: use different serializer for GET?
        return super().get_serializer_class()

    # Individual GET
    def retrieve(self, request, pk=None):
        queryset = Rating.objects.filter(driver=pk)
        ratings = queryset.all()
        serializer = RatingSerializer(ratings, many=True)

        # Calculate average rating value
        if len(ratings) > 0:
            average_rating = sum([r.value for r in ratings]) / len(ratings)
        else:
            average_rating = None

        # Add average rating to response data
        response_data = serializer.data
        response_data["average_rating"] = average_rating

        return Response(response_data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # NOTE: this saves the entity in the DB and returns the created object
        serializer.save()

        created_id = serializer.instance.id
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"id": created_id, **serializer.data},
            # self.get_serializer(driver_routine).data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )