from django.db import models

from users.models import User


class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - {self.routines.count()} routines"
