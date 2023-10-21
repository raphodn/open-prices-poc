from datetime import date

from django import forms

from prices.models import Price


class PriceCreateForm(forms.ModelForm):
    product_code = forms.CharField(min_length=13, max_length=13)
    currency = forms.ChoiceField(choices=[("€", "€")], initial="€", disabled=True)
    location_name = forms.CharField(widget=forms.widgets.Textarea(attrs={"rows": 2, "readonly": "readonly"}))
    location_osm_id = forms.IntegerField(label="OSM ID", widget=forms.widgets.NumberInput(attrs={"readonly": "readonly"}))
    date = forms.DateField(initial=date.today, widget=forms.widgets.DateInput(attrs={"class": "form-control", "type": "date"}))

    class Meta:
        model = Price
        fields = ["product_code", "price", "currency", "location_name", "location_osm_id", "date"]
