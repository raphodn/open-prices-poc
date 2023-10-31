import random
from datetime import date

import factory
import factory.fuzzy
from factory.django import DjangoModelFactory

from prices.models import Price


class PriceFactory(DjangoModelFactory):
    class Meta:
        model = Price

    product_code = factory.Faker("ean13")
    price = factory.LazyAttribute(lambda x: random.randrange(0, 100))
    # currency = factory.Faker("currency_symbol")
    currency = factory.fuzzy.FuzzyChoice([key for (key, value) in Price.CURRENCY_CHOICES])
    location_osm_id = factory.LazyAttribute(lambda x: random.randrange(100000, 999999999999))
    date = date.fromisoformat("2023-10-30")
