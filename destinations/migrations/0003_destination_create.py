# Generated by Django 5.2 on 2025-05-04 13:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_alter_destination_city_alter_destination_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
