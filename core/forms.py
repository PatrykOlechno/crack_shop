from django import forms
from django_countries.fields import CountryField

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'Paypal')
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Pocztowa"
    }))
    apartment_adress = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': '33'
    }))
    country = CountryField(blank_label='(select country)').formfield()
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '16-100 Sokółka'
    }))
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
