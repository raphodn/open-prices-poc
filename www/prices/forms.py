from datetime import date

from django import forms


class PriceCreateForm(forms.Form):
    product_code = forms.CharField(label="Product code", min_length=13, max_length=13)
    price = forms.CharField(label="Price")
    currency = forms.ChoiceField(choices=[("€", "€")], initial="€", disabled=True)
    location = forms.CharField()
    date = forms.DateField(initial=date.today, widget=forms.widgets.DateInput(attrs={"class": "form-control", "type": "date"}))
