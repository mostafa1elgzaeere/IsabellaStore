from django.db.models.base import Model
from django import forms
from order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['first_name', 'last_name', 'email', 'address', 'postal_code','city']


    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name .. "
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name .. "
        self.fields["email"].widget.attrs["placeholder"] = "Email .. "
        self.fields["address"].widget.attrs["placeholder"] = "Address .. "
        self.fields["city"].widget.attrs["placeholder"] = "City .. "
        self.fields["postal_code"].widget.attrs["placeholder"] = "Postal Code .. "
