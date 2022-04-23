from django.db import models

# Create your models here.


class Email(models.Model):
    mail = models.EmailField()


class PhoneNumber(models.Model):

    number = models.CharField(max_length=15, blank=True)


class User(models.Model):

    lastName = models.CharField(max_length=35)
    firstName = models.CharField(max_length=35)
    emails = models.ForeignKey(
        Email, on_delete=models.CASCADE, related_name="user_emails"
    )
    phoneNumbers = models.ForeignKey(
        PhoneNumber, on_delete=models.CASCADE, related_name="user_phone_numbers"
    )
    date_created = models.DateTimeField(auto_now_add=True)
