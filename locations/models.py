from django.db import models
from django.utils import timezone


class Location(models.Model):
    OSM_TYPE_NODE = "NODE"
    OSM_TYPE_WAY = "WAY"
    OSM_TYPE_RELATION = "RELATION"
    OSM_TYPE_CHOICES = [
        (OSM_TYPE_NODE, "Node"),
        (OSM_TYPE_WAY, "Way"),
        (OSM_TYPE_RELATION, "Relation"),
    ]

    osm_id = models.PositiveBigIntegerField(verbose_name="ID (OSM)")
    osm_type = models.CharField(verbose_name="Type (OSM)", choices=OSM_TYPE_CHOICES, blank=True, null=True)
    osm_display_name = models.CharField(verbose_name="Display name (OSM)", blank=True, null=True)
    osm_lat = models.DecimalField(
        verbose_name="Latitude (OSM)", max_digits=11, decimal_places=7, blank=True, null=True
    )
    osm_lon = models.DecimalField(
        verbose_name="Longitude (OSM)", max_digits=11, decimal_places=7, blank=True, null=True
    )

    created = models.DateTimeField(verbose_name="Creation date", default=timezone.now)
    updated = models.DateTimeField(verbose_name="Last update date", auto_now=True)

    class Meta:
        unique_together = ["osm_id", "osm_type"]
        verbose_name = "Location"
        verbose_name_plural = "Locations"
