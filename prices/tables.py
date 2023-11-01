import django_tables2 as tables

from common.tables import ImageColumn, TextEllipsisColumn
from prices.models import Price


TABLE_DEFAULT_TEMPLATE = "django_tables2/bootstrap5.html"
TABLE_DEFAULT_ATTRS = {"class": "table-responsive table-striped table-bordered border-primary font-size-small"}
CATEGORY_FIELD_SEQUENCE = [field.name for field in Price._meta.fields]


class PriceTable(tables.Table):
    product_off_image_url = ImageColumn()
    location_osm_name = TextEllipsisColumn(attrs={"td": {"title": lambda record: record.location_osm_name}})

    class Meta:
        model = Price
        fields = CATEGORY_FIELD_SEQUENCE
        sequence = CATEGORY_FIELD_SEQUENCE
        template_name = TABLE_DEFAULT_TEMPLATE
        attrs = TABLE_DEFAULT_ATTRS
