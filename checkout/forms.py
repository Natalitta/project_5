from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',)

    def __init__(self, *args, **kwargs):
        # To add placeholders and classes

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
        }

        # To set autofocus on first field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # To remove labels generated automatically
        for field in self.fields:

            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
