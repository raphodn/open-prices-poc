import django_tables2 as tables

from common.tables import ChoiceColumn
from prices.models import Price


TABLE_DEFAULT_TEMPLATE = "django_tables2/bootstrap5.html"
TABLE_DEFAULT_ATTRS = {"class": "table-responsive table-striped table-bordered border-primary font-size-small"}
CATEGORY_FIELD_SEQUENCE = [field.name for field in Price._meta.fields]


class PriceTable(tables.Table):
    class Meta:
        model = Price
        fields = CATEGORY_FIELD_SEQUENCE
        sequence = CATEGORY_FIELD_SEQUENCE
        template_name = TABLE_DEFAULT_TEMPLATE
        attrs = TABLE_DEFAULT_ATTRS

    def __init__(self, *args, **kwargs):
        for field_name in Price.CHOICE_FIELDS:
            self.base_columns[field_name] = ChoiceColumn()
        super().__init__(*args, **kwargs)
