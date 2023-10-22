from django.db import models
from django.utils import timezone


class Price(models.Model):
    CURRENCY_EURO = "€"
    CURRENCY_CHOICES = [(CURRENCY_EURO, CURRENCY_EURO)]

    product_code = models.CharField(verbose_name="Product code")

    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    currency = models.CharField(verbose_name="Currency", choices=CURRENCY_CHOICES, default=CURRENCY_EURO)

    location_name = models.CharField(verbose_name="Location name")
    location_osm_id = models.PositiveIntegerField(verbose_name="Location (OSM ID)")

    date = models.DateField(verbose_name="Date")

    created = models.DateTimeField(verbose_name="Creation date", default=timezone.now)

    class Meta:
        verbose_name = "Price"
        verbose_name_plural = "Prices"
