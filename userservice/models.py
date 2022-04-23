from django.db import models

# Create your models here.


class User(models.Model):

    lastName = models.CharField(max_length=35)
    firstName = models.CharField(max_length=35)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}"


class Email(models.Model):
    mail = models.EmailField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="user_emails"
    )

    def __str__(self) -> str:
        return f"{self.mail}"


class PhoneNumber(models.Model):

    number = models.CharField(max_length=15, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="user_phone_numbers"
    )

    def __str__(self) -> str:
        return f"{self.number}"
