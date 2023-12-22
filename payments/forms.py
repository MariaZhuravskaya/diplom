from django import forms
from payments.models import Payments


class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payments
        exclude = ('user', 'date',)
