from django.contrib import admin
from .models import Booking, Ticket

# Register your models here.
class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 1
class BookingAdmin(admin.ModelAdmin):
    inlines = (TicketInline,)
    list_display = ('user', 'event', 'booking_reference', 'status', 'total_amount', 'is_paid')
    search_fields = ('booking_reference', 'user__username', 'event__title')
    list_filter = ('status', 'is_paid')
admin.site.register(Booking, BookingAdmin)