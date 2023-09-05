from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.utils import timezone


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
        link = reverse(
            "users:email_verification",
            kwargs={
                "email": self.user.email,
                "code": self.code,
            },
        )
        verification_link = f"{settings.DOMAIN_NAME}/{link}"
        subject = f"Подтверждение учетной записи для {self.user.username}"
        message = "Для подтверждения почты {} перейдите по ссылке {}".format(
            self.user.email,
            verification_link,
        )
        send_mail(
            subject=subject,
            message=message,
            from_email="from@example.com",
            recipient_list=[self.user.email],
        )

    def is_expired(self) -> bool:
        if self.expiration >= timezone.now():
            return True
        else:
            return False
