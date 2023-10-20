from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from www.prices.forms import PriceCreateForm


class PriceCreateView(FormView):
    form_class = PriceCreateForm
    template_name = "prices/create.html"
    success_url = reverse_lazy("pages:home")
    success_message = "Price created!"

    def form_valid(self, form):
        print(form.cleaned_data)
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        return super().form_valid(form)
