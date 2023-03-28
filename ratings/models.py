from django.db import models
from trips.models import Trip
from drivers.models import Driver
from django.core.validators import MaxValueValidator, MinValueValidator

class Rating(models.Model):
    RATING_COMMENTS = (
        ('Buena conducción', 'Buena conducción'),
        ('Conductor agradable', 'Conductor agradable'),
        ('Ya nos conocíamos', 'Ya nos conocíamos'),
    )

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    comment = models.CharField(max_length=20, choices=RATING_COMMENTS, null=True, blank=True)
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.driver} - {self.trip} ({self.value})"