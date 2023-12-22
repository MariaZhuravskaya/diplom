from django import forms
from subscription.models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('user', 'is_active', 'payments',)
