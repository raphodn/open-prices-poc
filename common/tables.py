import django_tables2 as tables
from django.utils.html import format_html

from common.utils import get_choice_key, truncate_with_ellipsis
from prices.models import Price


PRICE_CHOICE_FIELD_MAPPING = {
    "currency": Price.CURRENCY_CHOICES,
    "location_osm_type": Price.OSM_TYPE_CHOICES,
    "source": Price.SOURCE_CHOICES,
}


class ChoiceColumn(tables.Column):
    def render(self, value, record, bound_column):
        value_title = value
        if type(record) is Price:
            if bound_column.name in PRICE_CHOICE_FIELD_MAPPING.keys():
                value_title = value
                value = get_choice_key(PRICE_CHOICE_FIELD_MAPPING[bound_column.name], value)
        return format_html(f'<span class="badge bg-primary" title="{value_title}">{value}</span>')


class TextEllipsisColumn(tables.Column):
    def render(self, value):
        return truncate_with_ellipsis(value, 60)


class ImageColumn(tables.Column):
    def render(self, value):
        return format_html(
            f'<a href="{value}" target="_blank" rel="noopener"><img src="{value}" title="{value}" height="100" /></a>'
        )
