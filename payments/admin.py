from django.contrib import admin
from payments.models import Payments


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('publication', 'user', 'date')
