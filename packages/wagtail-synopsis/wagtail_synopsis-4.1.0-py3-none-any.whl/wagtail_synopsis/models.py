import logging
import inspect

from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save, post_init, post_save, pre_delete
from django.dispatch import receiver

from django.db import models as django_models
from django.core.validators import MinValueValidator

from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.functional import cached_property, classproperty
from django.conf import settings

from taggit.models import TagBase, ItemBase

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel, ObjectList, InlinePanel
from wagtail.snippets.models import register_snippet

from django_auxiliaries.model_fields import MultipleChoiceField
from wagtail_block_model_field.fields import BlockModelField

from officekit import models as officekit # noqa

from .blocks import *  # We import blocks here so that the content block registration methods are called.
from .validators import validate_identifier, validate_category
from .mixins import SpecificMixin
from .fields import StaticField
from .apps import get_app_label

__all__ = ['Synopsis', 'PageSynopsis', 'build_synopsis_class_for', 'SynopsisAdapter',
           'sync_page_synopsis', 'determine_page_url', 'SynopsisTagItem', 'SynopsisTag']

APP_LABEL = get_app_label()

logger = logging.getLogger("passenger_wsgi")


class SynopsisTag(TagBase):
    class Meta:
        verbose_name = "synopsis tag"
        verbose_name_plural = "synopsis tags"


class SynopsisTagItem(ItemBase):

    class Meta:
        # constraints = [
        #    django_models.UniqueConstraint('content_object',
        #                                   'tag', name='unique_%(app_label)s_%(class)s.unique_tag_assignment')
        #]

        unique_together = (('content_object', 'tag'),)

    tag = django_models.ForeignKey(
        SynopsisTag, related_name="tagged_synopsis", on_delete=django_models.CASCADE
    )

    content_object = ParentalKey(
        to=APP_LABEL + '.Synopsis',
        on_delete=django_models.CASCADE,
        related_name='tagged_items'
    )


AUTHOR_ROLE = 'author'
EDITOR_ROLE = 'editor'

ROLES = (AUTHOR_ROLE, EDITOR_ROLE)
ROLE_CHOICES = ((AUTHOR_ROLE, "Author"), (EDITOR_ROLE, "Editor"))


def get_default_synopsis_content_type():
    """
    Returns the content type to use as a default for media items whose content type
    has been deleted.
    """
    return ContentType.objects.get_for_model(Synopsis)


# noinspection SpellCheckingInspection
@register_snippet
class Synopsis(SpecificMixin, Orderable, ClusterableModel):

    class Meta:
        verbose_name = 'synopsis'
        verbose_name_plural = 'synopses'

    AUTHOR_NAMES = 'author'
    EDITOR_NAMES = 'editor'

    NAMES_ROLES = [AUTHOR_NAMES, EDITOR_NAMES]

    @property
    def last_date_time(self):
        return self.updated_at if self.updated_at else self.created_at

    @property
    def timestamp_category(self):
        if self.updated_at == self.created_at:
            return "created"

        return "updated"

    @property
    def represents(self):

        if self.specific != self:
            return self.specific.represents

        return None

    @property
    def has_destination_url(self):

        if self.specific != self:
            url = self.specific.determine_destination_url()
        else:
            url = self.determine_destination_url()

        return bool(url)

    static = StaticField()
    # This is a placeholder so that the default unchanged form is accepted as an instance on post

    content_type = django_models.ForeignKey(
        ContentType,
        verbose_name=_('content type'),
        related_name='synopses',
        on_delete=django_models.SET(get_default_synopsis_content_type),
        editable=False
    )

    category = django_models.CharField(max_length=128, validators=[validate_identifier], default='')

    rubric = django_models.CharField(max_length=128, default='', blank=True)
    rubric_url = django_models.URLField(verbose_name=_("rubric URL"), default='', blank=True)

    heading = django_models.CharField(max_length=512, default='', blank=True)
    summary = RichTextField(default='', blank=True, editor=APP_LABEL + ".summary")

    visual = BlockModelField(VisualBlock(required=False), value_class=VisualBlockValue, blank=True, null=True)

    names = BlockModelField(NameListBlock(choices=ROLE_CHOICES, default_choice=AUTHOR_ROLE),
                            value_class=NameListBlockValue, blank=True, null=True)

    external_url = django_models.URLField(
        verbose_name=_("external URL"),
        default='',
        blank=True
    )

    tags = ClusterTaggableManager(through=APP_LABEL + '.SynopsisTagItem', blank=True)

    prominence_index = django_models.IntegerField(default=None,
                                                  validators=[
                                                        MinValueValidator(1)
                                                  ],
                                                  blank=True,
                                                  null=True)

    prominence_order = django_models.IntegerField(default=None,
                                                  validators=[
                                                        MinValueValidator(1)
                                                  ],
                                                  blank=True,
                                                  null=True)

    created_by_user = django_models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('created by user'),
        null=True,
        blank=True,
        editable=False,
        on_delete=django_models.SET_NULL
    )

    created_at = django_models.DateTimeField(
        verbose_name=_('created at'),
        default=None,
        editable=False)

    updated_at = django_models.DateTimeField(
        verbose_name=_('updated at'),
        blank=True,
        null=True,
        default=None,
        editable=False)

    metrics = django_models.JSONField(blank=True, null=True, default=dict)

    panels = [
        FieldPanel('category'),

        MultiFieldPanel([
            FieldPanel('heading'),
            FieldPanel('summary'),
            FieldPanel('tags')
        ], heading='Brief'
        ),

        FieldPanel('visual'),
        InlinePanel('name_index', heading="Indexed Names"),
        MultiFieldPanel([
            FieldPanel('external_url'),
        ], heading='Destination URL'
        ),

        MultiFieldPanel([
            FieldPanel('prominence_index'),
            FieldPanel('prominence_order'),
        ], heading='Prominence'
        )
    ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # noinspection PyUnresolvedReferences
        if not self.id:

            self.id = None
            self.created_at = timezone.now()
            self.updated_at = self.created_at

            # this model is being newly created
            # rather than retrieved from the db;
            # noinspection PyUnresolvedReferences
            if not self.content_type_id:

                # set content type to correctly represent the model class
                # that this was created as
                self.content_type_id = ContentType.objects.get_for_model(self).id

        self.deferred_name_assignments = []

    def determine_destination_url(self, request=None, current_site=None):

        if self.external_url:
            return self.external_url

        if not self.represents:
            return ''

        result = ''

        for adapter in self.specific_class.adapters:
            determine_url_method = adapter.get_determine_url_method(self.represents)

            if not determine_url_method:
                continue

            result = determine_url_method(request, current_site)
            break

        return result

    def save(self, **kwargs):

        for adapter in self.specific_class.adapters:
            sync_method = adapter.get_sync_method(self.represents)

            if not sync_method:
                continue

            sync_method(self)

        self.deferred_name_assignments = []

        json_value = self.specific_class.names.field.block_def.get_prep_value(self.names) # noqa

        role = json_value.get('role', None) # noqa

        self.index_names_from(json_value, role)

        super().save(**kwargs)

        self.clean_name_index(role)

        for assignment in self.deferred_name_assignments:
            assignment.synopsis = self.specific
            assignment.save()

        self.deferred_name_assignments = []

    @classproperty
    def adapters(cls):
        return cls._adapters

    @classmethod
    def install_synopsis_adapter_for(cls, editable_fields=None, sync_method=None, determine_url_method=None,
                                     tagged_item_class=None, tags_field='tags', tagged_items_field='tagged_items'):

        model_adapter = SynopsisAdapter()
        model_adapter.synopsis_class = cls
        model_adapter.editable_fields = editable_fields
        model_adapter.sync_method = sync_method
        model_adapter.determine_url_method = determine_url_method
        model_adapter.tagged_item_class = tagged_item_class
        model_adapter.tags_field = tags_field
        model_adapter.tagged_items_field = tagged_items_field

        cls.adapters.append(model_adapter)

        model_adapter.install_signal_handlers()

        return model_adapter

    @cached_property
    def name_assignment_model_class(self):
        return apps.get_model(APP_LABEL + ".nameinsynopsis")

    def create_name_assignment(self, family_name, given_names_and_initials, person, role):

        assignment = self.name_assignment_model_class(
                            synopsis_id=self.pk,
                            family_name=family_name,
                            given_names_and_initials=given_names_and_initials,
                            person_id=person.pk,
                            role=role)

        self.deferred_name_assignments.append(assignment)

    def clean_name_index(self, role):
        filters = {
            'synopsis_id': self.pk
        }

        if role:
            filters['role'] = role

        self.name_assignment_model_class.objects.filter(**filters).delete()

    def index_names_from(self, value, role):

        if value is None:
            return

        names = value.get("names", [])
        names = [name for name in names if name["type"] == "person"]

        for idx, name in enumerate(names):

            name_type = name['type']

            if name_type != 'person':
                continue

            person_name = name['value']

            given_names_and_initials = person_name['given_names_and_initials']
            family_name = person_name['family_name']

            given_names_and_initials = given_names_and_initials.strip()
            family_name = family_name.strip()

            identify_with = person_name.get("identify_with", None)

            person = None

            if identify_with:

                try:
                    person = officekit.Person.objects.get(pk=identify_with)
                except officekit.Person.DoesNotExist:
                    pass
            else:

                people = officekit.Person.objects.all().filter(
                    given_names_and_initials__iexact=given_names_and_initials,
                    family_name__iexact=family_name)

                n = people.count()

                if n == 1:
                    person = people[0]

            if person:

                given_names_and_initials = person.given_names_and_initials
                family_name = person.family_name

                given_names_and_initials = given_names_and_initials.strip()
                family_name = family_name.strip()

            self.create_name_assignment(family_name=family_name, given_names_and_initials=given_names_and_initials,
                                        person=person, role=role)

    def __str__(self):

        result = ''

        if self.category:
            result += '[{}] '.format(self.category)

        text = self.heading

        if not text:
            text = self.summary

        result += text
        result += " ▶ " + self.determine_destination_url()
        return result


@register_snippet
class NameInSynopsis(Orderable):

    class Meta(Orderable.Meta):
        verbose_name = 'Name in Synopsis'
        verbose_name_plural = 'Names in Synopsis'
        # constraints = [
        #    django_models.UniqueConstraint(fields=['synopsis', 'family_name', 'given_names_and_initials'],
        #                                   name='unique_%(app_label)s_%(class)s.name_assignment')
        #]

        unique_together = (('synopsis', 'family_name', 'given_names_and_initials'),)

    synopsis = ParentalKey(Synopsis, related_name="name_index", on_delete=django_models.CASCADE, blank=False)

    family_name = django_models.CharField("Family Name", default="", max_length=192, blank=False)
    given_names_and_initials = django_models.CharField("Given Name(s) and Initial(s)", default="", max_length=192, blank=False)

    person = django_models.ForeignKey(officekit.Person, related_name="synopses+",
                                      on_delete=django_models.SET_NULL, blank=True, null=True)

    role = MultipleChoiceField(choices=ROLE_CHOICES, default=AUTHOR_ROLE, blank=True, max_length=64)

    panels = [
        FieldPanel('synopsis'),
        FieldPanel('family_name'),
        FieldPanel('given_names_and_initials'),
        FieldPanel('person'),
        FieldPanel('role'),
    ]

    @classmethod
    def create(cls, synopsis, personal_name, person, role):

        result = cls(synopsis=synopsis, personal_name=personal_name, person=person, role=role)

        return result

    def __str__(self):
        return self.given_names_and_initials + " " + self.family_name + " in "  + self.synopsis.heading + (" [identified]" if self.person else "") # noqa


class SynopsisAdapter:

    synopsis_class = Synopsis
    editable_fields = None

    sync_method = None
    sync_method_name = 'sync_synopsis'

    determine_url_method = None
    determine_url_method_name = 'determine_url'

    tagged_item_class = None
    tags_field = None
    tagged_items_field = None

    @cached_property
    def synopsis_content_type(self):
        return ContentType.objects.get_for_model(self.synopsis_class)

    def create_synopsis(self):
        return self.synopsis_class()

    def get_synopsis_field_name(self, instance_or_class):
        synopsis_field_name = self.synopsis_class.model.field.remote_field.name
        synopsis_field_name = getattr(instance_or_class, 'synopsis_field_name', synopsis_field_name)
        return synopsis_field_name

    def get_synopsis_editable_fields(self, instance_or_class):
        synopsis_editable_fields = getattr(instance_or_class, 'synopsis_editable_fields', self.editable_fields)

        if synopsis_editable_fields is None:
            synopsis_editable_fields = list(self.synopsis_class._meta.fields)

        return synopsis_editable_fields

    def get_sync_method(self, instance):
        sync_method = getattr(instance, self.sync_method_name, None)

        if sync_method is None and self.sync_method:

            def sync_method(synopsis):
                return self.sync_method(instance, synopsis)

        if not callable(sync_method):
            return None

        return sync_method

    def get_determine_url_method(self, instance):
        determine_url_method = getattr(instance, self.determine_url_method_name, None)

        if determine_url_method is None and self.determine_url_method:

            def determine_url_method(request, current_site=None):
                return self.determine_url_method(instance, request, current_site=current_site)

        if not callable(determine_url_method):
            return None

        return determine_url_method

    def get_synopsis_relation(self, instance):
        synopsis_field_name = self.get_synopsis_field_name(instance)
        synopsis_relation = getattr(instance, synopsis_field_name, None)
        return synopsis_relation

    def create_synopsis_panel_for(self, model_class):

        synopsis_field_name = self.get_synopsis_field_name(model_class)
        synopsis_editable_fields = self.get_synopsis_editable_fields(model_class)

        synopsis_panel = ObjectList([
            InlinePanel(synopsis_field_name, min_num=1, max_num=1, panels=[
                             FieldPanel('static'),
                         ] + [FieldPanel(field) for field in
                              synopsis_editable_fields if field != 'static']
            )
        ],
            heading='Synopsis'
        )

        synopsis_panel = synopsis_panel.bind_to_model(model_class)

        return synopsis_panel

    # noinspection PyMethodMayBeStatic
    def tag_pre_delete(self, instance, **kwargs):

        if not instance.content_object.synopsis.exists():
            return

        try:
            shadow_tag = SynopsisTag.objects.get(name=instance.tag.name, slug=instance.tag.slug) # noqa
        except SynopsisTag.DoesNotExist: # noqa
            return

        for synopsis in instance.content_object.synopsis.all():

            shadow_items = SynopsisTagItem.objects.filter(content_object_id=synopsis.id, tag_id=shadow_tag.id) # noqa
            shadow_items.delete()

    # noinspection PyMethodMayBeStatic
    def synopsis_post_save(self, instance, **kwargs):

        for tag in getattr(instance.represents, self.tags_field).all():
            shadow_tag, _ = SynopsisTag.objects.get_or_create(name=tag.name, slug=tag.slug) # noqa

            shadow_item, created = SynopsisTagItem.objects.get_or_create( # noqa
                content_object_id=instance.id, tag_id=shadow_tag.id)

            if not created:
                continue

            getattr(instance, self.tagged_items_field).add(shadow_item)
            # print("Saving tag \'%s\' for \'%s\'" % (shadow_tag.name, instance.heading))

    def install_signal_handlers(self):

        if self.tagged_item_class is None or not self.tags_field or not self.tagged_items_field:
            return

        def synopsis_post_save_wrapper(instance, **kwargs):
            self.synopsis_post_save(instance, **kwargs)

        def tag_pre_delete_wrapper(instance, **kwargs):
            self.tag_pre_delete(instance, **kwargs)

        receiver(post_save, sender=self.synopsis_class)(synopsis_post_save_wrapper)
        receiver(pre_delete, sender=self.tagged_item_class)(tag_pre_delete_wrapper)


def build_synopsis_class_for(model_class,
                             field_on_model=None):

    if not isinstance(model_class, ClusterableModel):
        RuntimeError('Model class for Synopsis must be derived from ClusterableModel')

    name = model_class.__name__ + 'Synopsis'

    if not field_on_model:
        field_on_model = 'synopsis'

    stack = inspect.stack()[1]
    module = inspect.getmodule(stack[0])

    def represents(self):
        return self.model

    synopsis_class = type(name, (Synopsis,), {
        '__module__': module.__name__,
        'model': ParentalKey(model_class, related_name=field_on_model, on_delete=django_models.CASCADE, blank=False),
        'model_class': model_class,
        'represents': property(fget=represents),
        '_adapters': []
    })

    return synopsis_class

"""
def install_signal_handlers(model_class, model_adapter, exclude_models=None):

    if exclude_models is None:
        exclude_models = []

    stack = [(model_class, 0, None)]

    while stack:

        model, child_index, children = stack[-1]

        if children is None:

            children = list(model.__subclasses__())

            if model not in exclude_models:

                # print(model.__name__)

                decorator = receiver(post_init, sender=model)
                decorator(lambda signal, **kwargs: model_adapter.model_post_init(**kwargs))

                decorator = receiver(pre_save, sender=model)
                decorator(lambda signal, **kwargs: model_adapter.model_pre_save(**kwargs))

        if child_index >= len(children):
            stack.pop()
            continue

        stack[-1] = model, child_index + 1, children
        stack.append((children[child_index], 0, None))

    pass
"""


def sync_page_synopsis(page, synopsis):

    synopsis.category = getattr(page, 'synopsis_category', '')
    synopsis.heading = page.title
    synopsis.rubric = ''
    synopsis.rubric_url = ''

    synopsis.created_by_user = page.owner
    synopsis.created_at = page.first_published_at or timezone.now()
    synopsis.updated_at = page.last_published_at

    if not synopsis.summary:
        pass


def determine_page_url(page, request, current_site=None):
    return page.get_url(request=request, current_site=current_site)


PageSynopsis = build_synopsis_class_for(Page)
