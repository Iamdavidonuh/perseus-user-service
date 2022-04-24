from django.urls import path, include
from rest_framework import routers
from userservice import viewsets

router = routers.DefaultRouter()

router.register("users", viewsets.UserViewset, "users")
router.register("user-email", viewsets.UserEmailViewset, "user-email")
router.register(
    "user-phone-number", viewsets.UserPhoneNumberViewset, "user_phone_number"
)


urlpatterns = [
    path("", include(router.urls)),
    path(
        "user-emails/<int:user_pk>",
        viewsets.UserEmailViewset.as_view({"get": "retrieve"}),
        name="get-user-emails",
    ),
    path(
        "user-phone-numbers/<int:user_pk>",
        viewsets.UserPhoneNumberViewset.as_view({"get": "retrieve"}),
        name="get-user-phone-numbers",
    ),
]
