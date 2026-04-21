# payments/admin.py

from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('stripe_payment_id', 'amount', 'is_paid', 'created_at')
    list_filter = ('is_paid', 'created_at')
    search_fields = ('stripe_payment_id',)

# Register the Payment model with the admin site
admin.site.register(Payment, PaymentAdmin)