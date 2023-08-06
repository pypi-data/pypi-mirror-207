from django.db.models import CharField

from .form_fields import StaticFormField

__all__ = ['StaticField']


class StaticField(CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        kwargs['default'] = ''
        kwargs['blank'] = True
        kwargs['null'] = True
        kwargs['name'] = ''
        kwargs['verbose_name'] = ''
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "form_class": StaticFormField,
                **kwargs,
            }
        )
