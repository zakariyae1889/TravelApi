# Generated by Django 5.2 on 2025-05-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='destination',
            name='country',
            field=models.CharField(max_length=255),
        ),
    ]
