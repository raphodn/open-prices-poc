import django_tables2 as tables
from django.utils.html import format_html

from common.utils import truncate_with_ellipsis


class TextEllipsisColumn(tables.Column):
    def render(self, value):
        return truncate_with_ellipsis(value, 60)


class ImageColumn(tables.Column):
    def render(self, value):
        return format_html(
            f'<a href="{value}" target="_blank" rel="noopener"><img src="{value}" title="{value}" height="100" /></a>'
        )
