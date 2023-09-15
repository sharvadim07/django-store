import uuid
from datetime import timedelta

from celery import shared_task
from django.utils import timezone
from users.models import EmailVerification, User


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    code = uuid.uuid4()
    expiration = timezone.now() + timedelta(days=2)
    record = EmailVerification.objects.create(
        user=user,
        code=code,
        expiration=expiration,
    )
    record.send_verification_email()
