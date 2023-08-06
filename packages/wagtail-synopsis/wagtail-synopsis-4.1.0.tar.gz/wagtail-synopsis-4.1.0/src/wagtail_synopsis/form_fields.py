from django.forms import fields
from django.forms import widgets

__all__ = ['StaticFormField']


class StaticFormField(fields.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['widget'] = widgets.HiddenInput
        super().__init__(*args, **kwargs)

    def bound_data(self, data, initial):
        return ''

    def has_changed(self, initial, data):
        return True
