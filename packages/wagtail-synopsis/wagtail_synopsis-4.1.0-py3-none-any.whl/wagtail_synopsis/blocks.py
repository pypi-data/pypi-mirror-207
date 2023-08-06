import weakref

from django.conf import settings

from wagtail import blocks

from wagtail_tags_block.blocks import TagsBlock
from wagtail_switch_block import SwitchBlock, DynamicSwitchBlock
from wagtail_switch_block.block_registry import BlockRegistry

from wagtail_dynamic_choice.blocks import DynamicMultipleChoiceBlock

from wagtail_content_block.annotations import *
from wagtail_content_admin.blocks import ContentBlock, ContentBlockValue, register_content_block, ContentProviderBlockMixin

from media_catalogue.blocks import MediaItemChooserBlock, MediaItemChooserBlockValue

from querykit.base import *
from querykit.value_types import *
from querykit.value_sources import *
from querykit.forms import PickerFactory, SelectFactory, Choice

from csskit.blocks import SideBlock
from aldine.blocks import BaseContentLayoutBlock
from figurative.blocks import FigureBlock, SlideshowBlock
from officekit.blocks import NameListBlock as DefaultNameListBlock, NameListBlockValue as DefaultNameListBlockValue

from .apps import get_app_label
from .curation import CuratedSynopsis

__all__ = ['NameListBlock', 'NameListBlockValue',
           'VisualBlock', 'VisualBlockValue',
           'SynopsesBlock', 'SynopsesBlockValue', 'SynopsesLayoutBlock', 'SynopsisListBlock',
           'register_curator_block', # noqa
           'StandardCuratorBlock']

APP_LABEL = get_app_label()

NameListBlockValue = DefaultNameListBlockValue


class NameListBlock(DefaultNameListBlock):

    class Meta:
        classname = settings.WAGTAIL_SYNOPSIS_NAMES_CLASSNAME

    role = blocks.ChoiceBlock(choices=[], default=None, required=False)

    def __init__(self, local_blocks=None, choices=None, default_choice=None, **kwargs):

        if choices is None:
            choices = []

        if local_blocks:
            local_block_dict = dict(local_blocks)
        else:
            local_block_dict = {}

        local_block_dict["role"] = blocks.ChoiceBlock(choices=choices, default=default_choice)

        local_blocks = local_block_dict.items()

        self.constructor_kwargs_ = kwargs

        super().__init__(local_blocks, **kwargs)

        self.constructor_kwargs_["choices"] = choices
        self.constructor_kwargs_["default_choice"] = default_choice

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


VISUAL_ANNOTATIONS = ContentAnnotations(groups=[

            ContentAnnotationGroup(
                identifier='credits',
                label='Credits',
                fields=[
                    TextAnnotationField(
                        identifier='category',
                        label='',
                        default_value='Image',
                        attributes={
                            'placeholder': ''
                        }
                    ),

                    TextAreaAnnotationField(
                        identifier='names',
                        label='Name(s)',
                        attributes={
                            'placeholder': ''
                        }
                    )
                ]
            )
        ])


VisualBlockValue = MediaItemChooserBlockValue


class VisualBlock(MediaItemChooserBlock):

    class Meta:
        annotations = VISUAL_ANNOTATIONS


class CuratorBlockRegistry(BlockRegistry):

    # noinspection PyMethodMayBeStatic
    def should_include_entry_for_switch_block(self, identifier, entry, switch_block):
        return True

    # noinspection PyMethodMayBeStatic
    def instantiate_block(self, identifier, entry, switch_block):

        block_kwargs = dict(entry.block_kwargs)

        block = entry.block_type(*entry.block_args, **block_kwargs)
        block.set_name(identifier)

        return block


CURATOR_BLOCK_REGISTRY = CuratorBlockRegistry()
CURATOR_BLOCK_REGISTRY.define_procedures_in_caller_module("curator")


Synopsis = None


class CuratorBlock(ContentProviderBlockMixin, blocks.StructBlock):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, target_model=APP_LABEL + ".synopsis", **kwargs)

    # noinspection PyMethodMayBeStatic
    def derive_content(self, value, request=None):

        global Synopsis

        if Synopsis is None:
            from .models import Synopsis

        items, _ = self.select(value, Synopsis.objects.all())
        annotations = self.clean_annotations(items)
        return self.create_content(items=items, annotations=annotations)

    # noinspection PyMethodMayBeStatic
    def select(self, curator_value, query_set, request=None):

        global Synopsis

        if Synopsis is None:
            from .models import Synopsis

        return query_set, Synopsis.objects.none()


MAIN_PROMINENCE_INDEX = 1
MAJOR_PROMINENCE_INDEX = 2
MINOR_PROMINENCE_INDEX = 3


class StandardCuratorBlock(CuratorBlock):

    class Meta:
        prominence_css_class_map = {
            MAIN_PROMINENCE_INDEX: 'main',
            MAJOR_PROMINENCE_INDEX: 'major',
            MINOR_PROMINENCE_INDEX: 'minor',
        }
        prominence_slots_map = {
            MAIN_PROMINENCE_INDEX: 2,
            MAJOR_PROMINENCE_INDEX: 2,
            MINOR_PROMINENCE_INDEX: 5,
    }

    categories = DynamicMultipleChoiceBlock(label="Categories", default=[], required=False,
                                            choices_function_name=APP_LABEL + ".curation.get_synopsis_category_choices")

    tags = TagsBlock(tag_model=APP_LABEL + ".synopsistag", required=False, help_text="Select Tagged Synopses Only")

    def select(self, curator_value, query_set, request=None):

        filter_options = {
            'content_object_id__in': query_set.values_list('id', flat=True),
        }

        curator_tag_names = [tag.name for tag in curator_value['tags']]

        if curator_tag_names:
            filter_options['tag__name__in'] = curator_tag_names

            selected_ids = [item.content_object_id for item in SynopsisTagItem.objects.all(). # noqa
                prefetch_related('tag', 'content_object').filter(
                **filter_options
            )]

            selected = query_set.filter(id__in=selected_ids)
        else:
            selected = query_set

        filter_options = {}
        categories = curator_value['categories']

        if categories:
            filter_options['category__in'] = categories

        if filter_options:
            selected = selected.filter(**filter_options)

        selected = selected.order_by('prominence_index', 'prominence_order', '-updated_at')

        prominence_orders = {}
        prominence_css_class_map = dict(self.meta.prominence_css_class_map)
        prominence_slots_map = dict(self.meta.prominence_slots_map)

        curated_selection = []

        for index, item in enumerate(selected):

            curated = CuratedSynopsis(item)

            if not curated.prominence_index:
                curated.prominence_index = 1

            slots = None
            assigned_slot = False

            while slots is None and prominence_slots_map:
                slots = prominence_slots_map.get(curated.prominence_index, None)

                if slots is None:
                    curated.prominence_index += 1
                    continue

                if slots > 0:
                    assigned_slot = True
                    slots -= 1
                    if slots > 0:
                        prominence_slots_map[curated.prominence_index] = slots
                    else:
                        del prominence_slots_map[curated.prominence_index]
                    break

                curated.prominence_index = curated.prominence_index + 1

            if not assigned_slot:
                break

            curated.prominence_order = prominence_orders.setdefault(curated.prominence_index, 0) + 1
            prominence_orders[curated.prominence_index] = curated.prominence_order

            curated.prominence_css_class = prominence_css_class_map.get(curated.prominence_index, '')
            curated_selection.append(curated)

        selected_ids = [curated.id for curated in curated_selection]

        return curated_selection, query_set.exclude(id__in=selected_ids)


register_curator_block(APP_LABEL, "standard", StandardCuratorBlock, [], {}) # noqa


def configure_chooser_synopsis_item(item, instance):

    from .content_admin import synopsis_admin
    synopsis_admin.configure_frontend_item(item, instance)


def create_synopsis_query_parameters():

    order_choices = [OrderSpecifier("date_descending", "↓ Date",
                                    PathValueSource(value_type=DateTimeType, path='-updated_at')
                                    ),

                     OrderSpecifier("date_ascending", "↑ Date",
                                    PathValueSource(value_type=DateTimeType, path='updated_at')
                                    ),

                     OrderSpecifier("title", "↑ Title",
                                    PathValueSource(value_type=TextType, path='heading')
                                    )
                     ]

    select_factory = SelectFactory()

    fp_factory = PickerFactory()

    parameters = [
        ResultSliceParameter(
               identifier='page',
               widget_factory=None),

        OrderParameter(
               identifier='sort_by',
               label='Sort By',
               order_specifiers=order_choices,
               widget_factory=select_factory),

        SliceSizeParameter(
               identifier='per_page',
               label='Per Page',
               size_choices=[
                    Choice(25, "25"),
                    Choice(50, "50"),
                    Choice(100, "100"),
                    Choice('all', "All")
               ],
               widget_factory=select_factory),

        Filter(identifier='author',
               label='Author',
               value_source=PathValueSource(value_type=TextType,
                                            path='name_index.family_name',
                                            label_path='name_index.family_name'),
               widget_factory=fp_factory),

        # Filter(identifier='rubric',
        #       label='Rubric',
        #       value_source=PathValueSource(value_type=TextType, path='rubric'),
        #       widget_factory=fp_factory),

        # Filter(identifier='updated_at',
        #       label='Date',
        #       value_source=PathValueSource(value_type=DateTimeType, path='updated_at'),
        #       widget_factory=fp_factory),

        Filter(identifier='keyword',
               label='Keyword',
               value_source=PathValueSource(value_type=TextType, path='tags.slug', label_path='tags.name'),
               widget_factory=fp_factory)
    ]

    return parameters


def create_synopsis_query_widgets():

    widgets = [
        "clear", "submit"
    ]

    return widgets


SynopsesBlockValue = ContentBlockValue


class SynopsesBlock(ContentBlock):

    class Meta:
        verbose_item_name = "Synopsis"
        verbose_item_name_plural = "Synopses"

        chooser_url = APP_LABEL + ':chooser'
        configure_function_name = APP_LABEL + '.blocks.configure_chooser_synopsis_item'
        max_num_choices = None
        chooser_prompts = {
            'add': 'Add Synopsis',
            'replace': 'Replace Synopsis'
        }

        chooser_filter = None
        content_choice_blocks_function_name = APP_LABEL + '.blocks.curator_block_choices'

        query_field_choices = [
            ('category', 'Category'),
            ('heading', 'Heading'),
            ('summary', 'Summary'),
            ('updated_at', 'Updated Date Time'),
            ('rubric', 'Rubric'),
            ('tags__name', 'Tag Name'),
        ]
        query_slice_size = 25
        query_parameters = create_synopsis_query_parameters()
        query_form_widgets = create_synopsis_query_widgets()
        query_form_classname = settings.WAGTAIL_SYNOPSIS_SYNOPSES_QUERY_FORM_CLASSNAME

    def __init__(self, **kwargs):
        super().__init__(target_model=APP_LABEL + ".synopsis", **kwargs)  # noqa


register_content_block(APP_LABEL, "synopses", SynopsesBlock, [], {}, item_type=APP_LABEL + ".Synopsis")  # noqa


class SynopsisStyleBlock(blocks.StructBlock):

    # synopsis = blocks.StaticBlock()  # placeholder

    def get_context(self, value, parent_context=None):
        context = super(SynopsisStyleBlock, self).get_context(value, parent_context)
        return context


class VisualSynopsisBlock(SynopsisStyleBlock):

    class Meta:
        template = APP_LABEL + "/blocks/visual_synopsis.html"

    visual_placement = SideBlock(required=False, label="Visual Placement")

    show_publishing_date = blocks.BooleanBlock(required=False, label="Show Publishing Date")
    show_authors = blocks.BooleanBlock(required=False, label="Show Authors")
    show_rubrics = blocks.BooleanBlock(required=False, label="Show Rubrics")
    show_tags = blocks.BooleanBlock(required=False, label="Show Tags")

    visuals = SwitchBlock(local_blocks=[
        ('figures', FigureBlock(user_configurable_content=False)),
        ('slideshow', SlideshowBlock(user_configurable_content=False))],
        default_block_name='slideshow',
        template=APP_LABEL + "/blocks/visual_synopsis_switch.html")


class TextualSynopsisBlock(SynopsisStyleBlock):

    class Meta:
        template = APP_LABEL + "/blocks/textual_synopsis.html"

    show_publishing_date = blocks.BooleanBlock(required=False, label="Show Publishing Date")
    show_authors = blocks.BooleanBlock(required=False, label="Show Authors")
    show_rubrics = blocks.BooleanBlock(required=False, label="Show Rubrics")
    show_tags = blocks.BooleanBlock(required=False, label="Show Tags")


class SynopsisStyleBlockRegistry(BlockRegistry):

    # noinspection PyMethodMayBeStatic
    def should_include_entry_for_switch_block(self, identifier, entry, switch_block):
        return True

    # noinspection PyMethodMayBeStatic
    def instantiate_block(self, identifier, entry, switch_block):

        block_kwargs = dict(entry.block_kwargs)

        block_kwargs["user_configurable_content"] = False

        block = entry.block_type(*entry.block_args, **block_kwargs)
        block.set_name(identifier)

        return block


SYNOPSIS_STYLE_BLOCK_REGISTRY = SynopsisStyleBlockRegistry()
SYNOPSIS_STYLE_BLOCK_REGISTRY.define_procedures_in_caller_module("synopsis_style")

register_synopsis_style_block(APP_LABEL, "visual", VisualSynopsisBlock, [], {}) # noqa
register_synopsis_style_block(APP_LABEL, "textual", TextualSynopsisBlock, [], {}) # noqa


class SynopsesLayoutBlock(BaseContentLayoutBlock):

    class Meta:
        classname = settings.WAGTAIL_SYNOPSIS_SYNOPSES_LAYOUT_BLOCK_CLASSNAME
        tag_classname = settings.WAGTAIL_SYNOPSIS_TAG_CLASSNAME
        supported_item_types = [APP_LABEL + ".synopsis"]

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


class SynopsisListBlock(SynopsesLayoutBlock):
    class Meta:
        classname = settings.WAGTAIL_SYNOPSIS_SYNOPSIS_LIST_BLOCK_CLASSNAME
        content_wrapper_classname = settings.WAGTAIL_SYNOPSIS_SYNOPSIS_LIST_CONTENT_WRAPPER_CLASSNAME
        template = APP_LABEL + "/blocks/synopsis_list.html"

    synopsis_style = DynamicSwitchBlock(child_blocks_function_name=APP_LABEL + ".blocks.synopsis_style_block_choices",
                                      choice_label="Select")

    def __init__(self, *args, **kwargs):

        self.base_blocks['synopsis_style'].container_block = weakref.ref(self)

        super().__init__(*args, **kwargs)

