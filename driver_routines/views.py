from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status, viewsets
from rest_framework.response import Response

from driver_routines.models import DriverRoutine
from driver_routines.serializers import DriverRoutineSerializer


# TODO: For making this endpoint login-protected, add the following:
# from django.contrib.auth.mixins import LoginRequiredMixin
# class DriverRoutineViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
class DriverRoutineViewSet(viewsets.ModelViewSet):
    queryset = DriverRoutine.objects.all()
    serializer_class = DriverRoutineSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return DriverRoutineSerializer  # TODO: use different serializer for GET?
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
