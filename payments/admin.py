from django.contrib import admin
from .models import Payment

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'payment_method', 'transaction_id', 'status', 'payment_date')
    search_fields = ('transaction_id', 'booking__booking_reference', 'booking__user__username')
    list_filter = ('payment_method', 'status')
admin.site.register(Payment, PaymentAdmin)