from django.db.models import signals
from django.test import TestCase
from django.urls import reverse

from prices.factories import PriceFactory
from prices.models import Price, price_post_create_fetch_info
from products.models import Product, product_post_create_fetch_info


PRICE_JSON = {"product_code": "0123456789101", "price": 3.5, "location_osm_id": 652825274, "date": "2023-10-30"}


class PriceCreateApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        signals.post_save.disconnect(price_post_create_fetch_info, sender=Price)
        signals.post_save.disconnect(product_post_create_fetch_info, sender=Product)
        pass

    def test_price_create(self):
        self.assertEqual(Price.objects.count(), 0)
        url = reverse("api:prices-list")  # anonymous user
        price_data = PRICE_JSON.copy()
        response = self.client.post(url, data=price_data, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Price.objects.count(), 1)
        price = Price.objects.last()
        self.assertEqual(price.source, "API")
        # self.assertEqual(Product.objects.count(), 1)

    def test_price_create_readonly_fields(self):
        url = reverse("api:prices-list")  # anonymous user
        # try to force a custom "source"
        price_data = PRICE_JSON.copy()
        price_data["source"] = "CUSTOM"
        response = self.client.post(url, data=price_data, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Price.objects.count(), 1)
        price = Price.objects.last()
        self.assertEqual(price.source, "API")
        # try to pass a custom "location_osm_name"
        price_data = PRICE_JSON.copy()
        price_data["location_osm_name"] = "CUSTOM"
        response = self.client.post(url, data=price_data, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Price.objects.count(), 1 + 1)
        price = Price.objects.last()
        self.assertEqual(price.location_osm_name, None)


class PriceListApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        signals.post_save.disconnect(price_post_create_fetch_info, sender=Price)
        signals.post_save.disconnect(product_post_create_fetch_info, sender=Product)
        PriceFactory()
        PriceFactory()

    def test_price_list(self):
        url = reverse("api:prices-list")  # anonymous user
        response = self.client.get(url)
        self.assertEqual(response.data["count"], 2)
        self.assertEqual(len(response.data["results"]), 2)
        self.assertFalse("id" in response.data["results"][0])
        self.assertFalse("source" in response.data["results"][0])
        for field_name in Price.SERIALIZED_FIELDS:
            self.assertTrue(field_name in response.data["results"][0])


class PriceListFilterApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        signals.post_save.disconnect(price_post_create_fetch_info, sender=Price)
        signals.post_save.disconnect(product_post_create_fetch_info, sender=Product)
        PriceFactory(product_code="1111111111111", price=1.0, date="2023-10-01")
        PriceFactory(product_code="2222222222222", price=2.5, date="2023-10-02")
        PriceFactory(product_code="3333333333333", price=3.25, date="2023-10-03")
        PriceFactory(product_code="4444444444444", price=4, date="2023-10-04")
        PriceFactory(product_code="5555555555555", price=5, date="2023-10-05")

    def test_price_list_filter_by_product_code(self):
        url = reverse("api:prices-list") + "?product_code=1111111111111"
        response = self.client.get(url)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(len(response.data["results"]), 1)

    def test_price_list_filter_by_price(self):
        # exact price
        url = reverse("api:prices-list") + "?price=4"
        response = self.client.get(url)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(len(response.data["results"]), 1)
        # lt / gt / lte / gte
        url = reverse("api:prices-list") + "?price__gte=4"
        response = self.client.get(url)
        self.assertEqual(response.data["count"], 1 + 1)
        self.assertEqual(len(response.data["results"]), 1 + 1)

    def test_price_list_filter_by_date(self):
        url = reverse("api:prices-list") + "?date=2023-10-02"
        response = self.client.get(url)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(len(response.data["results"]), 1)
