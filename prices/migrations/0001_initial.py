# Generated by Django 4.2.6 on 2023-10-21 21:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Price",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_code", models.CharField(verbose_name="Product code")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Price"
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[("€", "€")], default="€", verbose_name="Currency"
                    ),
                ),
                ("location_name", models.CharField(verbose_name="Location name")),
                (
                    "location_osm_id",
                    models.PositiveIntegerField(verbose_name="Location (OSM ID)"),
                ),
                ("date", models.DateField(verbose_name="Date")),
                (
                    "created",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Creation date"
                    ),
                ),
            ],
            options={
                "verbose_name": "Price",
                "verbose_name_plural": "Prices",
            },
        ),
    ]
