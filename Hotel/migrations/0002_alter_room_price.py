# Generated by Django 5.2 on 2025-05-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
