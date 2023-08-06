from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property

__all__ = ['SpecificMixin']


class SpecificMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.id: # noqa

            self.id = None

            if hasattr(self.__class__, 'content_type') and not self.content_type_id: # noqa

                self.content_type_id = ContentType.objects.get_for_model(self).id

    @property
    def cached_content_type(self):
        """
        .. versionadded:: 2.10

        Return this media_item's ``content_type`` value from the ``ContentType``
        model's cached manager, which will avoid a database query if the
        object is already in memory.
        """
        return ContentType.objects.get_for_id(
                self.content_type_id)  # noqa

    @cached_property
    def specific_class(self):
        """
        Return the class that this media item would be if instantiated in its
        most specific form.

        If the model class can no longer be found in the codebase, and the
        relevant ``ContentType`` has been removed by a database migration,
        the return value will be ``None``.

        If the model class can no longer be found in the codebase, but the
        relevant ``ContentType`` is still present in the database (usually a
        result of switching between git branches without running or reverting
        database migrations beforehand), the return value will be ``None``.
        """
        return self.cached_content_type.model_class()

    @cached_property
    def specific(self):
        """
        Returns this media_item in its most specific subclassed form with all field
        values fetched from the database. The result is cached in memory.
        """
        return self.get_specific()

    @cached_property
    def specific_deferred(self):
        """
        .. versionadded:: 2.12

        Returns this media_item in its most specific subclassed form without any
        additional field values being fetched from the database. The result
        is cached in memory.
        """
        return self.get_specific(deferred=True)

    def get_specific(self, deferred=False, copy_attrs=None):
        """
        .. versionadded:: 2.12

        Return this media_item in its most specific subclassed form.

        By default, a database query is made to fetch all field values for the
        specific object. If you only require access to custom methods or other
        non-field attributes on the specific object, you can use
        ``deferred=True`` to avoid this query. However, any attempts to access
        specific field values from the returned object will trigger additional
        database queries.

        If there are attribute values on this object that you wish to be copied
        over to the specific version (for example: evaluated relationship field
        values, annotations or cached properties), use `copy_attrs`` to pass an
        iterable of names of attributes you wish to be copied.

        If called on a media_item object that is already an instance of the most
        specific class (e.g. an ``EventPage``), the object will be returned
        as is, and no database queries or other operations will be triggered.

        If the media_item was originally created using a media_item type that has since
        been removed from the codebase, a generic ``Page`` object will be
        returned (without any custom field values or other functionality
        present on the original class). Usually, deleting these pages is the
        best course of action, but there is currently no safe way for Wagtail
        to do that at migration time.
        """

        model_class = self.specific_class

        if model_class is None:
            # The codebase and database are out of sync (e.g. the model exists
            # on a different git branch and migrations were not applied or
            # reverted before switching branches). So, the best we can do is
            # return the media_item in it's current form.
            return self

        if isinstance(self, model_class):
            # self is already the an instance of the most specific class
            return self

        if deferred:
            # Generate a tuple of values in the order expected by __init__(),
            # with missing values substituted with DEFERRED ()
            values = tuple(
                getattr(self, f.attname, self.pk if f.primary_key else DEFERRED)  # noqa
                for f in model_class._meta.concrete_fields
            )
            # Create object from known attribute values
            specific_obj = model_class(*values)
            specific_obj._state.adding = self._state.adding  # noqa
        else:
            # Fetch object from database
            specific_obj = model_class._default_manager.get(id=self.id)  # noqa

        # Copy additional attribute values
        for attr in copy_attrs or ():
            if attr in self.__dict__:
                setattr(specific_obj, attr, getattr(self, attr))

        return specific_obj

