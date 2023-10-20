from django.urls import path

from www.prices.views import PriceCreateView


app_name = "prices"

urlpatterns = [
    path("create/", PriceCreateView.as_view(), name="create"),
]
