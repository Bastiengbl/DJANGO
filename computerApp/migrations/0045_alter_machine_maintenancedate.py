# Generated by Django 4.1.7 on 2023-05-20 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0044_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 20, 10, 56, 48, 911932)
            ),
        ),
    ]
