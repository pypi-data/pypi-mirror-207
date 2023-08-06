import re

from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

__all__ = ['validate_identifier', 'validate_category']


def validate_identifier(value):

    if re.search(r"(^[^A-Za-z0-9_]|\s)", value):

        raise ValidationError(
            _("Identifiers must start with a letter, a digit or underscore "
              "and cannot contain whitespace characters: {:}").format(value)
        )


def validate_category(value):

    if re.search(r"(^[^A-Za-z0-9_]|\s)", value):

        raise ValidationError(
            _("Categories must start with a letter, a digit or underscore "
              "and cannot contain whitespace characters: {:}").format(value)
        )