# Generated by Django 4.2.6 on 2023-10-31 10:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prices", "0002_alter_price_location_osm_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="location_name",
            field=models.CharField(blank=True, verbose_name="Location name"),
        ),
    ]
