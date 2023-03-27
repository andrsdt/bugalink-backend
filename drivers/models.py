from django.db import models

from driver_routines.models import DriverRoutine
from users.models import User


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Routines is a list of routines that the driver has
    routines = models.ForeignKey(DriverRoutine, on_delete=models.CASCADE)
    # vehicles = models.OneToManyField(Vehicle, on_delete=models.CASCADE, related_name="driver")
    # preferences = models.OneToOneField(DriverPreference, on_delete=models.CASCADE, related_name="driver")
    # Sworn declaration, DNI, driver license, entry date as driver...

    def __str__(self):
        return f"{self.user.email} - {self.routines.count()} routines"
