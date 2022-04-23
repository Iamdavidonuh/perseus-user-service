from rest_framework import viewsets
from userservice import serializers
from userservice.models import User


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs.update({"partial": True})
        return super().get_serializer(*args, **kwargs)
