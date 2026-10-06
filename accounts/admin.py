from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "get_full_name", "role", "phone", "is_active")
    list_filter = ("role", "is_active", "is_staff")
    search_fields = ("username", "first_name", "last_name", "email", "phone")
    fieldsets = BaseUserAdmin.fieldsets + (("SchoolRun", {"fields": ("role", "phone")}),)
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("SchoolRun", {"fields": ("role", "phone", "first_name", "last_name", "email")}),
    )
