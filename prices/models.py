from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Price(models.Model):
    CURRENCY_EURO = "€"
    CURRENCY_CHOICES = [(CURRENCY_EURO, CURRENCY_EURO)]
    SOURCE_FORM = "FORM"
    SOURCE_API = "API"
    SOURCE_CHOICES = [(SOURCE_FORM, "Form"), (SOURCE_API, "API")]

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

    OSM_TYPE_NODE = "NODE"
    OSM_TYPE_WAY = "WAY"
    OSM_TYPE_RELATION = "RELATION"
    OSM_TYPE_CHOICES = [
        (OSM_TYPE_NODE, "Node"),
        (OSM_TYPE_WAY, "Way"),
        (OSM_TYPE_RELATION, "Relation"),
    ]

    CHOICE_FIELDS = ["product_off_db", "currency", "location_osm_type", "source"]
    SERIALIZED_FIELDS = [
        "product_code",
        "product_off_name",
        "product_off_image_url",
        "price",
        "currency",
        "location_osm_id",
        "location_osm_type",
        "location_osm_name",
        "location_osm_lat",
        "location_osm_lon",
        "date",
        "created",
    ]
    READONLY_FIELDS = [
        "product_in_off",
        "product_off_db",
        "product_off_name",
        "product_off_image_url",
        "location_osm_type",
        "location_osm_name",
        "location_osm_lat",
        "location_osm_lon",
        "source",
        "created",
    ]

    product_code = models.CharField(verbose_name="Product code")
    product_in_off = models.BooleanField(verbose_name="Product in OFF?", blank=True, null=True)
    product_off_db = models.CharField(verbose_name="Product OFF DB", choices=OFF_SOURCE_CHOICES, blank=True, null=True)
    product_off_name = models.CharField(verbose_name="Product name (OFF)", blank=True, null=True)
    product_off_image_url = models.URLField(verbose_name="Product image URL (OFF)", blank=True, null=True)

    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    currency = models.CharField(verbose_name="Currency", choices=CURRENCY_CHOICES, default=CURRENCY_EURO)

    location_osm_id = models.PositiveBigIntegerField(verbose_name="Location ID (OSM)")
    location_osm_type = models.CharField(
        verbose_name="Location type (OSM)", choices=OSM_TYPE_CHOICES, blank=True, null=True
    )
    location_osm_name = models.CharField(verbose_name="Location name (OSM)", blank=True, null=True)
    location_osm_lat = models.DecimalField(
        verbose_name="Location latitude (OSM)", max_digits=11, decimal_places=7, blank=True, null=True
    )
    location_osm_lon = models.DecimalField(
        verbose_name="Location longitude (OSM)", max_digits=11, decimal_places=7, blank=True, null=True
    )

    date = models.DateField(verbose_name="Date")

    source = models.CharField(verbose_name="Source", choices=SOURCE_CHOICES, default=SOURCE_FORM)

    created = models.DateTimeField(verbose_name="Creation date", default=timezone.now)

    class Meta:
        verbose_name = "Price"
        verbose_name_plural = "Prices"


@receiver(post_save, sender=Price)
def price_post_create_fetch_info(sender, instance, created, **kwargs):
    if created:
        if instance.product_code:
            from prices.tasks import fetch_and_update_product_info_from_openfoodfacts

            fetch_and_update_product_info_from_openfoodfacts(instance)
        if instance.location_osm_id:
            from prices.tasks import fetch_and_update_location_info_from_openstreetmap

            fetch_and_update_location_info_from_openstreetmap(instance)
