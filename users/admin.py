from django.contrib import admin

from users.models import User, Payments, Subscription


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone', 'avatar', 'is_active',)
    search_fields = ('last_name', 'email', 'is_active',)
    list_filter = ('last_name', 'email',)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_date', 'payment_amount', 'payment_method',)
    list_filter = ('paid_course', 'paid_lesson', 'payment_method',)
    search_fields = ('user',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course',)
    list_filter = ('course',)
    search_fields = ('user',)