
from django.db import transaction


def replicate_tags(tags, tag_class):
    tag_names = [tag.name for tag in tags]
    result = []

    with transaction.atomic():
        for tag_name in tag_names:
            try:
                replicated_tag = tag_class.objects.all().get(name=tag_name)
            except tag_class.DoesNotExist:
                replicated_tag = tag_class(name=tag_name)
                replicated_tag.save()

            result.append(replicated_tag)

    return result


def apply_synopsis_tags_to_model(synopsis_tags, model, model_tag_class, model_tag_item_class):
    model_tags = replicate_tags(synopsis_tags.all(), model_tag_class)
    model_items = []

    for model_tag in model_tags:
        model_item = model_tag_item_class(tag=model_tag, content_object=model)
        model_items.append(model_item)

    model.tagged_items = model_items

