from django.contrib import admin
from .models import ContactMessage

# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at', 'is_resolved')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('is_resolved',)
admin.site.register(ContactMessage, ContactMessageAdmin)