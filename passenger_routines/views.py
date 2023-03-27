from rest_framework import status, viewsets
from rest_framework.response import Response

from passenger_routines.models import PassengerRoutine
from passenger_routines.serializers import PassengerRoutineSerializer

# TODO: For making this endpoint login-protected, add the following:
# from django.contrib.auth.mixins import LoginRequiredMixin
# class PassengerRoutineViewSet(LoginRequiredMixin, viewsets.ModelViewSet):


class PassengerRoutineViewSet(viewsets.ModelViewSet):
    queryset = PassengerRoutine.objects.all()
    serializer_class = PassengerRoutineSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return PassengerRoutineSerializer  # TODO: use different serializer for GET?
        return super().get_serializer_class()

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
