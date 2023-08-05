from __future__ import annotations

import importlib
import uuid
from typing import Any

from django.core import exceptions, checks, validators
from django.core.exceptions import ObjectDoesNotExist
from django.db import models, connection
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from cross_database_field.forms import CrossDatabaseFormField


class CrossField(models.Field):
    def __init__(self, to: str, remote_db: str, verbose_name=None, **kwargs):
        self.to = to
        self.remote_db = remote_db
        super().__init__(verbose_name, **kwargs)

    def from_db_value(self, value, expression, connection):
        """
        Parses a UUID value, and returns the remote model of it. Used on code occurrences, ej:
        "Model.objects.first().cross_field", where cross_field is this field.
        """
        if value is None:
            return None
        return self.parse_field(value)

    def formfield(self, **kwargs):
        """
        Sets the Form Field to use in the admin to edit the object.
        """

        model = self._parse_model()

        return super().formfield(
            **{
                "form_class": CrossDatabaseFormField,
                "queryset": model.objects.using(self.remote_db),
                "required": not self.null,
                **kwargs,
                "blank": self.blank,
            }
        )

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['to'] = self.to
        kwargs['remote_db'] = self.remote_db
        return name, path, args, kwargs

    def check(self, **kwargs):
        return [
            *super().check(**kwargs),
            *self._check_internal(**kwargs),
        ]

    def _check_internal(self, **kwargs) -> list:
        errors = []

        if self.primary_key is True:
            errors.append(
                checks.Error(
                    "CrossDatabaseFields cannot be the primary key of a model.",
                    obj=self,
                    id="cdf.E1",
                )
            )

        try:
            self._parse_model()
        except ModuleNotFoundError:
            errors.append(
                checks.Error(
                    "CrossDatabaseField 'to' parameter cannot be imported. (Currently: {})".format(self.to),
                    hint="Check the path in the 'to' param",
                    obj=self,
                    id="cdf.E3",
                )
            )

        return errors

    def _parse_model(self):
        callable_path = self.to.rsplit(".", 1)
        module = importlib.import_module(callable_path[0])
        return getattr(module, callable_path[1])

    def parse_field(self, remote_id: Any):
        """
        Parses a UUID object, and returns the remote model
        """
        model = self._parse_model()
        try:
            return model.objects.using(self.remote_db).get(pk=remote_id)
        except ObjectDoesNotExist:
            return None


class CrossDatabaseField(CrossField):
    empty_strings_allowed = False
    default_error_messages = {
        "invalid": _("“%(value)s” value must be an integer."),
    }
    description = 'Numeric cross database field'

    def __init__(self, to: str, remote_db: str, verbose_name=None, **kwargs):
        """
        A numeric based cross database field.

        To get started, declare a Model in another database, with a numeric pk, then pass
        the path as the "to" param, and the database name as "remote_db".

        Again, use this when the remote model primary key is of a numeric (Integer) type. By default,
        the primary key of all models is a number, so this should apply to anything right away.

        :param to: Path to model, as a string. Ej: "app.models.MyModel".
        :param remote_db: Database to read the model from, as declared in settings.
        :param verbose_name: Name to represent this field.
        :param kwargs: Django positional arguments.
        """
        super().__init__(to, remote_db, verbose_name, **kwargs)

    def check(self, **kwargs):
        return [
            *super().check(**kwargs),
            *self._check_max_length_warning(),
        ]

    def _check_max_length_warning(self):
        if self.max_length is not None:
            return [
                checks.Warning(
                    "'max_length' is ignored when used with %s."
                    % self.__class__.__name__,
                    hint="Remove 'max_length' from field",
                    obj=self,
                    id="fields.W122",
                )
            ]
        return []

    @cached_property
    def validators(self):
        # These validators can't be added at field initialization time since
        # they're based on values retrieved from `connection`.
        validators_ = super().validators
        internal_type = self.get_internal_type()
        min_value, max_value = connection.ops.integer_field_range(internal_type)
        if min_value is not None and not any(
                (
                        isinstance(validator, validators.MinValueValidator)
                        and (
                                validator.limit_value()
                                if callable(validator.limit_value)
                                else validator.limit_value
                        )
                        >= min_value
                )
                for validator in validators_
        ):
            validators_.append(validators.MinValueValidator(min_value))
        if max_value is not None and not any(
                (
                        isinstance(validator, validators.MaxValueValidator)
                        and (
                                validator.limit_value()
                                if callable(validator.limit_value)
                                else validator.limit_value
                        )
                        <= max_value
                )
                for validator in validators_
        ):
            validators_.append(validators.MaxValueValidator(max_value))
        return validators_

    def get_prep_value(self, value) -> int | None:
        value = super().get_prep_value(value)

        try:
            return int(value)
        except (TypeError, ValueError) as e:
            raise e.__class__(
                "Field '%s' expected a number but got %r." % (self.name, value),
            ) from e

    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        return connection.ops.adapt_integerfield_value(value, self.get_internal_type())

    def get_internal_type(self):
        return "BigIntegerField"

    def to_python(self, value):
        return self._parse_int(value)

    def _parse_int(self, value):
        if value is None:
            return value
        try:
            return int(value)
        except (TypeError, ValueError):
            raise exceptions.ValidationError(
                self.error_messages["invalid"],
                code="invalid",
                params={"value": value},
            )


class UUIDCrossDatabaseField(CrossField):
    default_error_messages = {
        'invalid': '“%(value)s” is not a valid UUID.',
    }
    description = 'Read-only cross database field'
    empty_strings_allowed = False

    def __init__(self, to: str, remote_db: str, verbose_name=None, **kwargs):
        """
        A UUID based cross database field.

        To get started, declare a Model in another database, with a UUIDField as pk, then pass
        the path as the "to" param, and the database name as "remote_db".

        Again, use this when the remote model primary key is of UUID type.

        :param to: Path to model, as a string. Ej: "app.models.MyModel".
        :param remote_db: Database to read the model from, as declared in settings.
        :param verbose_name: Name to represent this field.
        :param kwargs: Django positional arguments.
        """
        kwargs['max_length'] = 32
        super().__init__(to, remote_db, verbose_name, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs

    def clean(self, value, model_instance):
        """
        Convert the value's type and run validation. Validation errors
        from to_python() and validate() are propagated. Return the correct
        value if no error is raised.
        """
        value = self._return_uuid(value)
        self.validate(value, model_instance)
        self.run_validators(value)
        return value

    def get_internal_type(self):
        return "UUIDField"

    def get_prep_value(self, value) -> uuid.UUID:
        value = super().get_prep_value(value)

        return self._return_uuid(value)

    # def get_db_prep_save(self, value, connection):
    #     super().get_db_prep_save(value, connection)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is None:
            return None
        if not isinstance(value, uuid.UUID):
            value = self._return_uuid(value)

        if connection.features.has_native_uuid_field:
            return value
        return value.hex

    def to_python(self, value):
        """
        Takes any compatible value, parses it to `uuid.UUID`, and returns it.
        Used on code occurrences.
        """
        return self._parse_uuid(value)

    def _return_uuid(self, value):
        """
        Takes any compatible value, parses it to uuid. UUID, and returns it.
        Used in Forms display.
        """
        return self._parse_uuid(value)

    def _parse_uuid(self, value) -> uuid.UUID:
        """
        Parses a compatible object, and returns a UUID object
        """

        if value is not None and not isinstance(value, uuid.UUID):
            input_form = 'int' if isinstance(value, int) else 'hex'
            try:
                value = uuid.UUID(**{input_form: value})
            except (AttributeError, ValueError):
                raise exceptions.ValidationError(
                    self.error_messages['invalid'],
                    code='invalid',
                    params={'value': value},
                )
        return value


class CrossDatabaseCapableModel(models.Model):
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):

        # Convert to their remote PKs
        for field in self.__class__._meta.get_fields():
            if not issubclass(field.__class__, CrossField):
                continue

            value = getattr(self, field.name)

            if isinstance(value, models.Model):
                setattr(self, field.name, value.pk)

        super().save(force_insert, force_update, using, update_fields)

        # Convert back to instances, where possible
        for field in self.__class__._meta.get_fields():
            if not issubclass(field.__class__, CrossField):
                continue
            value = getattr(self, field.name)

            if isinstance(value, int) or isinstance(value, uuid.UUID):
                setattr(self, field.name, field.parse_field(value))

    class Meta:
        abstract = True


__all__ = [
    'CrossDatabaseField',
    'UUIDCrossDatabaseField',
    'CrossDatabaseCapableModel'
]
