from rest_framework import serializers

from userservice import models, utils


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = [
            "id",
            "mail",
            "user",
        ]


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhoneNumber
        fields = [
            "id",
            "number",
            "user",
        ]


class UserSerializer(serializers.ModelSerializer):
    user_emails = EmailSerializer(many=True)
    user_phone_numbers = PhoneNumberSerializer(many=True)

    class Meta:
        model = models.User
        exclude = [
            "date_created",
        ]

    def create(self, validated_data: dict):
        emails = validated_data.pop("user_emails")
        phone_numbers = validated_data.pop("user_phone_numbers")
        instance = models.User.objects.create(**validated_data)
        utils.create_related_data(instance, models.Email, emails)
        utils.create_related_data(instance, models.PhoneNumber, phone_numbers)
        return instance

    def to_representation(self, instance):

        response = {
            "id": instance.id,
            "lastName": instance.lastName,
            "firstName": instance.firstName,
            "emails": list(
                instance.user_emails.all().values_list("mail", flat=True).distinct()
            ),
            "phoneNumbers": list(
                instance.user_phone_numbers.all()
                .values_list("number", flat=True)
                .distinct()
            ),
        }
        return response
