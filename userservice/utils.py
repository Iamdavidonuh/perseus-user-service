from typing import Union
from django.db import models
from userservice import models


def create_related_data(
    instance: models.User, model: Union[models.PhoneNumber, models.Email], payload: dict
):
    """Creates entiries either in the phonenumber or email table using the user instance as a FK

    Args:
        instance (models.User): instance of user model
        model (Union[models.PhoneNumber, models.Email]): either the class phone number or email
        payload (dict): dictionary containing model data to save
    """

    for item in payload:
        model_object = model.objects.create(**item)
        model_object.user = instance
        model_object.save()
