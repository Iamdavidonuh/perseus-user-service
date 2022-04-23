from django.urls import path, include
from rest_framework import routers
from userservice import viewsets

router = routers.DefaultRouter()

router.register("users", viewsets.UserViewset, "users")


urlpatterns = [
    path("", include(router.urls)),
]
