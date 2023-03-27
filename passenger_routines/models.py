from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _

from locations.models import Location


class PassengerRoutine(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    departure_time_start = models.TimeField(_("Departure time window begin"))
    departure_time_end = models.TimeField(_("Departure time window end"))
    origin = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        related_name="origin_routines_passenger",
        null=True,
    )
    destination = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        related_name="destination_routines_passenger",
        null=True,
    )
    days_of_week = ArrayField(
        models.CharField(
            choices=(
                ("Mon", _("Monday")),
                ("Tue", _("Tuesday")),
                ("Wed", _("Wednesday")),
                ("Thu", _("Thursday")),
                ("Fri", _("Friday")),
                ("Sat", _("Saturday")),
                ("Sun", _("Sunday")),
            ),
            max_length=7,
            verbose_name=_("Day of week"),
        )
    )

    def __str__(self):
        return f"{self.origin} to {self.destination}"