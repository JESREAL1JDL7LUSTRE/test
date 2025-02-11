from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("id", "email", "first_name", "last_name", "is_staff", "is_superuser", "created_at")
    list_filter = ("is_staff", "is_superuser")  # ✅ Filter to show regular users & admins separately
    ordering = ("id",)
    search_fields = ("email", "first_name", "last_name")

    fieldsets = (
        (None, {"fields": ("email", "password", "clerk_id")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "image_url")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active")}),
        ("Important Dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )

    def get_queryset(self, request):
        """Show all users but separate them in the filter."""
        qs = super().get_queryset(request)
        return qs  # ✅ This keeps all users in one place but allows filtering

# ✅ Use `@admin.register(User)` Instead of `admin.site.register(User)`
@admin.register(User)
class UserAdminView(CustomUserAdmin):
    pass  # This will use the logic from `CustomUserAdmin`
