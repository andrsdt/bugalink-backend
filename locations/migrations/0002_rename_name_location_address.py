# Generated by Django 4.1.7 on 2023-03-27 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="location",
            old_name="name",
            new_name="address",
        ),
    ]
