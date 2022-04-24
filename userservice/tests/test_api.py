from ast import arg
from django.urls import reverse
from rest_framework import status

from userservice import serializers
from userservice.tests import TestBase
from userservice import models


class TestUserViewsets(TestBase):
    def setUp(self) -> None:
        self.user = self._create_user()

    def test_create_user_api_call_succeeds(self):
        response = self.api_client.post(
            reverse("users-list"),
            data=dict(
                firstName="Testing",
                lastName="User",
                user_emails=[
                    {"mail": "tuser@mail.com"},
                ],
                user_phone_numbers=[
                    {
                        "number": "08019320932",
                    }
                ],
            ),
            format="json",
        )
        user = models.User.objects.filter(id=response.data["id"]).first()
        self.assertIsNotNone(user)

    def test_get_all_users(self):
        """Test List API call"""
        response = self.api_client.get(reverse("users-list"), format="json")
        users = models.User.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_user_succeeds(self):
        """Tests the retrieve API call"""
        response = self.api_client.get(
            reverse("users-detail", args=(self.user.id,)), format="json"
        )
        user = models.User.objects.get(id=self.user.id)
        serializer = serializers.UserSerializer(user)
        self.assertEqual(response.data, serializer.data)

    def test_update_user_api_call_succeeds(self):
        """Test Put API call"""

        response = self.api_client.put(
            reverse("users-detail", args=(self.user.id,)),
            data=dict(lastName="updated test"),
            format="json",
        )
        user = models.User.objects.get(id=self.user.id)
        self.assertEqual(response.data["lastName"], user.lastName)

    def test_delete_api_call_succeeds(self):
        response = self.api_client.delete(reverse("users-detail", args=(self.user.id,)))
        user = models.User.objects.filter(id=self.user.id).first()
        self.assertIsNone(user)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestUserEmailsViewsets(TestBase):
    def setUp(self) -> None:
        self.email = self._create_user_email()

    def test_create_user_email_api_call_succeeds(self):
        response = self.api_client.post(
            reverse("user-email-list"),
            data=dict(mail="example@example.com", user=self.email.user.id),
            format="json",
        )
        email = models.Email.objects.filter(id=response.data["id"]).first()
        self.assertIsNotNone(email)

    def test_get_all_user_emails(self):
        """Test List API call"""
        response = self.api_client.get(
            reverse("get-user-emails", args=(self.email.user.id,)), format="json"
        )
        emails = models.Email.objects.filter(user=self.email.user).all()
        serializer = serializers.EmailSerializer(emails, many=True)

        self.assertEqual(response.data, serializer.data)

    def test_get_user_email(self):
        """Test Retrieve API call"""
        response = self.api_client.get(
            reverse("user-email-detail", args=(self.email.user.id,)), format="json"
        )
        email = models.Email.objects.get(id=self.email.id)
        serializer = serializers.EmailSerializer(email)

        self.assertEqual(response.data, serializer.data)

    def test_update_user_email_call_succeeds(self):
        """Test Put API call"""

        response = self.api_client.put(
            reverse("user-email-detail", args=(self.email.id,)),
            data=dict(mail="updated@yahoo.com"),
            format="json",
        )
        email = models.Email.objects.get(id=self.email.id)
        self.assertEqual(response.data["mail"], email.mail)

    def test_delete_api_call_succeeds(self):
        response = self.api_client.delete(
            reverse("user-email-detail", args=(self.email.id,))
        )
        email = models.Email.objects.filter(id=self.email.id).first()
        self.assertIsNone(email)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestUserPhoneNumberViewsets(TestBase):
    def setUp(self) -> None:
        self.phone = self._create_user_phone_number()

    def test_create_user_phone_number_api_call_succeeds(self):
        response = self.api_client.post(
            reverse("user_phone_number-list"),
            data=dict(number="999123", user=self.phone.user.id),
            format="json",
        )
        phone_number = models.PhoneNumber.objects.filter(id=response.data["id"]).first()
        self.assertIsNotNone(phone_number)

    def test_get_all_user_phone_numbers(self):
        """Test List API call"""
        response = self.api_client.get(
            reverse("get-user-phone-numbers", args=(self.phone.user.id,)), format="json"
        )
        phone_numbers = models.PhoneNumber.objects.filter(user=self.phone.user).all()
        serializer = serializers.PhoneNumberSerializer(phone_numbers, many=True)

        self.assertEqual(response.data, serializer.data)

    def test_get_user_email(self):
        """Test Retrieve API call"""
        response = self.api_client.get(
            reverse("user_phone_number-detail", args=(self.phone.user.id,)),
            format="json",
        )
        phone = models.PhoneNumber.objects.get(id=self.phone.id)
        serializer = serializers.PhoneNumberSerializer(phone)

        self.assertEqual(response.data, serializer.data)

    def test_update_user_email_call_succeeds(self):
        """Test Put API call"""

        response = self.api_client.put(
            reverse("user_phone_number-detail", args=(self.phone.id,)),
            data=dict(number="112-911"),
            format="json",
        )
        phone_number = models.PhoneNumber.objects.get(id=self.phone.id)
        self.assertEqual(response.data["number"], phone_number.number)

    def test_delete_api_call_succeeds(self):
        response = self.api_client.delete(
            reverse("user_phone_number-detail", args=(self.phone.id,))
        )
        phone_number = models.PhoneNumber.objects.filter(id=self.phone.id).first()
        self.assertIsNone(phone_number)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
