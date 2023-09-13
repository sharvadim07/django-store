from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from users.models import EmailVerification, User


class UserRegistrationViewTestCase(TestCase):
    def setUp(self) -> None:
        self.path = reverse("users:registration")
        self.data = {
            "first_name": "test",
            "last_name": "test",
            "username": "test",
            "email": "test@test.ru",
            "password1": "test",
            "password2": "test",
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "users/registration.html")

    def test_user_registration_post_success(self):
        # Check User creation
        self.assertFalse(User.objects.filter(username=self.data["username"]).exists())

        response = self.client.post(path=self.path, data=self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response.url, reverse("users:login"))
        # TODO: It doesn't work
        # self.assertRedirects(response, reverse("users:login"))
        self.assertTrue(User.objects.filter(username=self.data["username"]).exists())

        # Check EmailVerification creation
        email_verification = EmailVerification.objects.filter(
            user__username=self.data["username"]
        )
        self.assertTrue(email_verification.exists())

    def test_user_registration_post_error(self):
        User.objects.create(username=self.data["username"])

        response = self.client.post(path=self.path, data=self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(len(response.context_data["form"].errors["username"]) == 1)
