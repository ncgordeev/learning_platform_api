from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone', 'avatar', 'is_active',)
    search_fields = ('last_name', 'email', 'is_active',)
    list_filter = ('last_name', 'email',)
