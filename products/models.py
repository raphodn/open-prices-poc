from django.db import models
from django.utils import timezone


class Product(models.Model):
    OFF_SOURCE_OFF = "OFF"
    OFF_SOURCE_OPF = "OPF"
    OFF_SOURCE_OPFF = "OPFF"
    OFF_SOURCE_OBF = "OBF"
    OFF_SOURCE_CHOICES = [
        (OFF_SOURCE_OFF, "OpenFoodFacts"),
        (OFF_SOURCE_OPF, "OpenProductFacts"),
        (OFF_SOURCE_OPFF, "OpenPetFoodFacts"),
        (OFF_SOURCE_OBF, "OpenBeautyFacts"),
    ]

    code = models.CharField(verbose_name="Product code", primary_key=True, editable=False)

    in_off = models.BooleanField(verbose_name="Product in OFF?", blank=True, null=True)
    off_db = models.CharField(verbose_name="Product OFF DB", choices=OFF_SOURCE_CHOICES, blank=True, null=True)

    off_name = models.CharField(verbose_name="Product name (OFF)", blank=True, null=True)
    off_image_url = models.URLField(verbose_name="Product image URL (OFF)", blank=True, null=True)

    created = models.DateTimeField(verbose_name="Creation date", default=timezone.now)
    updated = models.DateTimeField(verbose_name="Last update date", auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
