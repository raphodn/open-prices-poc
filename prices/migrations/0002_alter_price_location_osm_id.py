# Generated by Django 4.2.6 on 2023-10-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prices", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="location_osm_id",
            field=models.PositiveBigIntegerField(verbose_name="Location (OSM ID)"),
        ),
    ]
