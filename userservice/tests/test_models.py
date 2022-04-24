from django.urls import reverse
from rest_framework import status
from userservice import serializers
from userservice.models import Email, PhoneNumber, User
from userservice.tests import TestBase


class TestModels(TestBase):
    def setUp(self) -> None:
        super().setUp()
        self.user = self._create_user()

    def test_user_gets_created(self):
        user = User.objects.create(lastName="test", firstName="user")
        query = User.objects.get(id=user.id)
        self.assertIsNotNone(query)

    def test_email_gets_created(self):
        email = Email.objects.create(user=self.user, mail="test@example.com")
        query = Email.objects.get(id=email.id)
        self.assertIsNotNone(query)

    def test_create_phone_number_succeeds(self):
        number = PhoneNumber.objects.create(user=self.user, number="829209932")
        query = PhoneNumber.objects.get(id=number.id)
        self.assertIsNotNone(query)
