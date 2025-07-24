from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'rating', 'approved', 'created_at')
    search_fields = ('user__username', 'event__title', 'comment')
    list_filter = ('rating', 'approved')
admin.site.register(Review, ReviewAdmin)