from django.contrib import admin

# Register your models here.
from users.models import User, EmailVerification


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username",)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "user",
        "expiration",
    )
    fields = (
        "code",
        "user",
        "expiration",
        "created_at",
    )
    readonly_fields = ("created_at",)
