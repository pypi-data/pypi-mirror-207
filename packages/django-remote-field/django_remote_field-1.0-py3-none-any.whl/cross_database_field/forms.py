import uuid

from django import forms
from django.core.exceptions import ValidationError
from django.db import models


class CrossDatabaseFormField(forms.ModelChoiceField):
    def prepare_value(self, value):
        if value is None:
            return None
        if isinstance(value, str):
            return value
        if isinstance(value, uuid.UUID):
            return str(value)
        if not isinstance(value, models.Model):
            return "Invalid"
        return str(value.pk)

    def to_python(self, value):
        if value == "":
            return None
        if value is None:
            raise ValidationError(
                "This field was assigned to a remote object that doesn't exist anymore. Please assign a new object.",
                code="invalid_choice",
                params={"value": value},
            )
        return value
