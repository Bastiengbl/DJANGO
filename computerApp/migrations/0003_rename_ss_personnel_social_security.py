# Generated by Django 4.1.7 on 2023-04-07 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0002_personnel_rename_pc_machine_ip"),
    ]

    operations = [
        migrations.RenameField(
            model_name="personnel",
            old_name="ss",
            new_name="social_security",
        ),
    ]
