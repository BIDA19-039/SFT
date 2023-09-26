from django.forms import ModelForm
from django import forms
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields=['featured_image','customer_name', 'customer_surname', 'customer_phone', 'customer_email','account']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        for customer_name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})