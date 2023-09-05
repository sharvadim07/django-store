from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self) -> str:
        return f"EmailVerification object for {self.user.email}"

    def send_verification_email(self):
        send_mail(
            "Subject here",
            "Test email verification.",
            "from@example.com",
            [self.user.email],
        )
