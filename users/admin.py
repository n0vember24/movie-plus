from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

from .models import User


@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = ('phone_number', 'first_name', 'email', 'is_staff')
    ordering = ("phone_number",)
    readonly_fields = ('image_preview',)


    def image_preview(self, model: User) -> str:
        if model.image:
            return format_html('<img src="%s" width="50" height="50"', model.image.url)
        return None

    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (_("Personal info"), {
            "fields": ("first_name", "last_name", "username", "email", "image", "image_preview")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "password1", "password2"),
            },
        ),
    )

    class Meta:
        verbose_name_plural = 'Моя аутентификация и авторизация'