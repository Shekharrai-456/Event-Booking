from django.contrib import admin
from .models import CustomUser , UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    
    
class CustomUserAdmin(admin.ModelAdmin):  # Corrected class name
    inlines = (UserProfileInline,)  # Corrected inline declaration
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('user_type', 'is_active')
admin.site.register(CustomUser , CustomUserAdmin)  # Corrected class name