from django import forms

class PaymentForm(forms.Form):
    ewallet_number = forms.CharField(label='E-Wallet Number', max_length=20)
    # Anda dapat menambahkan field tambahan lainnya sesuai kebutuhan
