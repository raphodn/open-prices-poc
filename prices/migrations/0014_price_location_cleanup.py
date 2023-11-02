# Generated by Django 4.2.6 on 2023-11-02 13:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("prices", "0013_price_location_migrate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="price",
            name="location_osm_lat",
        ),
        migrations.RemoveField(
            model_name="price",
            name="location_osm_lon",
        ),
        migrations.RemoveField(
            model_name="price",
            name="location_osm_name",
        ),
    ]