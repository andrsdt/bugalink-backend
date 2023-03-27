from django.db import models

from passenger_routines.models import PassengerRoutine
from users.models import User


class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    routines = models.ForeignKey(
        PassengerRoutine, on_delete=models.CASCADE, related_name="passenger"
    )

    def __str__(self):
        return f"{self.user.email} - {self.routines.count()} routines"
