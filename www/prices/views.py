from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django_tables2.views import SingleTableView

from prices.models import Price
from prices.tables import PriceTable
from www.prices.forms import PriceCreateForm


class PriceListView(SingleTableView):
    model = Price
    template_name = "prices/list.html"
    context_object_name = "prices"
    table_class = PriceTable


class PriceCreateView(CreateView):
    form_class = PriceCreateForm
    template_name = "prices/create.html"
    success_url = reverse_lazy("pages:home")
    success_message = "Price created!"

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        return super().form_valid(form)
