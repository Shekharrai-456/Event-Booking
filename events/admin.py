from django.contrib import admin
from .models import Event, Category, EventGallery

# Register your models here.
class EventGalleryInline(admin.TabularInline):
    model = EventGallery
    extra = 1
class EventAdmin(admin.ModelAdmin):
    inlines = (EventGalleryInline,)
    list_display = ('title', 'organizer', 'start_datetime', 'end_datetime', 'status')
    search_fields = ('title', 'description', 'location')
    list_filter = ('status', 'categories', 'start_datetime')
admin.site.register(Event, EventAdmin)
admin.site.register(Category)