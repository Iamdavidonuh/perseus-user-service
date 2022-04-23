from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, response
from userservice import serializers
from userservice.models import Email, PhoneNumber, User


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs.update({"partial": True})
        return super().get_serializer(*args, **kwargs)


class UserEmailViewset(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = serializers.EmailSerializer
    queryset = Email.objects.all()

    def retrieve(self, request, *args, **kwargs):
        if "user_pk" in self.kwargs:
            user_pk = self.kwargs.get("user_pk")
            user = get_object_or_404(User, pk=user_pk)
            serializer = serializers.EmailSerializer(user.user_emails.all(), many=True)
            return response.Response(serializer.data)
        return super().retrieve(request, *args, **kwargs)


class UserPhoneNumberViewset(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = serializers.PhoneNumberSerializer
    queryset = PhoneNumber.objects.all()

    def retrieve(self, request, *args, **kwargs):
        if "user_pk" in kwargs:
            user_pk = self.kwargs.get("user_pk")
            user = get_object_or_404(User, pk=user_pk)
            serializer = serializers.PhoneNumberSerializer(
                user.user_phone_numbers.all(), many=True
            )
            return response.Response(serializer.data)
        return super().retrieve(request, *args, **kwargs)
