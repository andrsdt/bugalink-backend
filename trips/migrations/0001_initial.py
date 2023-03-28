# Generated by Django 4.1.7 on 2023-03-27 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("passengers", "0003_alter_passenger_user"),
        ("driver_routines", "0002_driverroutine_driver"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trip",
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
                ("departure_datetime", models.DateTimeField()),
                (
                    "driver_routine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trips",
                        to="driver_routines.driverroutine",
                    ),
                ),
                (
                    "passengers",
                    models.ManyToManyField(
                        related_name="trips", to="passengers.passenger"
                    ),
                ),
            ],
        ),
    ]