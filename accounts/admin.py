from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Role info", {"fields": ("role",)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
