from django.test import TestCase
from rest_framework.test import APIClient

from userservice.models import Email, PhoneNumber, User


class TestBase(TestCase):
    """contains helper functions for all test cases"""

    api_client = APIClient()

    @staticmethod
    def _create_user(first_name=None, last_name=None):

        return User.objects.create(
            firstName=first_name or "samuel", lastName=last_name or "tests"
        )

    def _create_user_phone_number(self, phone_number=None):

        user = self._create_user()
        return PhoneNumber.objects.create(
            user=user, number=phone_number or "9920822092"
        )

    def _create_user_email(self, email=None):
        user = self._create_user()
        return Email.objects.create(user=user, mail=email or "test@example.com")
