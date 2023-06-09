# Generated by Django 4.1.7 on 2023-03-27 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("passengers", "0002_remove_passenger_routines"),
        ("passenger_routines", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="passengerroutine",
            name="passenger",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="routines",
                to="passengers.passenger",
            ),
        ),
    ]
