from django.contrib import admin
from subscription.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('publication', 'user', 'is_active', 'payments')
