from django.contrib import admin
from authentication.models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('username','first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined','email_verified')
    search_fields = ('username','first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined','email_verified')
    list_per_page =25



admin.site.register(User, UserAdmin)