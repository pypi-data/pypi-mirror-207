
from model_porter.config import ModelPorterConfig
from model_porter.utilities import define_tags as define_generic_tags
from model_porter.repository import UndefinedReference

from .models import SynopsisTag, SynopsisTagItem


def define_tags(*, tag_values, context):
    return define_generic_tags(tag_values=tag_values, tag_class=SynopsisTag, tag_item_class=SynopsisTagItem, context=context)


def create_synopsis(*, model, context, for_object):

    for_object_instance = context.get_instance(for_object, None)

    if for_object_instance is None:
        raise UndefinedReference(for_object)

    try:
        result = for_object_instance.synopsis.get()
    except model.DoesNotExist:
        result = model()
        for_object_instance.synopsis.add(result)

    return result


class WagtailSynopsisConfig(ModelPorterConfig):

    def __init__(self, app_label, module):
        super(WagtailSynopsisConfig, self).__init__(app_label, module)
        self.register_function_action(create_synopsis, context_argument='context')
        self.register_function_action(define_tags, context_argument='context')

