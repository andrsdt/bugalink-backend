# Generated by Django 4.1.7 on 2023-03-27 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("passengers", "0003_alter_passenger_user"),
        ("trips", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TripRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_recurrent", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PENDING", "PENDING"),
                            ("ACCEPTED", "ACCEPTED"),
                            ("REJECTED", "REJECTED"),
                            ("FINISHED", "FINISHED"),
                        ],
                        default="PENDING",
                        max_length=10,
                    ),
                ),
                ("note", models.CharField(blank=True, max_length=2000)),
                (
                    "passenger",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trip_requests",
                        to="passengers.passenger",
                    ),
                ),
                (
                    "trip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="requests",
                        to="trips.trip",
                    ),
                ),
            ],
        ),
    ]