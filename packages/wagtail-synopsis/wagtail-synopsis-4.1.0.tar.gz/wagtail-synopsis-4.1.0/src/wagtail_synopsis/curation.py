
from django.apps import apps


__all__ = ['register_synopsis_category', 'get_synopsis_category_choices', 'CuratedSynopsis']


SYNOPSIS_CATEGORIES = dict()


class SynopsisCategory:

    @property
    def identifier(self):
        return self.app_label + ":" + self.local_identifier

    def __init__(self, app_label, local_identifier, name):

        self.app_label = app_label
        self.local_identifier = local_identifier
        self.name = name

        app = apps.get_app_config(self.app_label)
        self.app_name = app.verbose_name


def register_synopsis_category(app_label, local_identifier, name):

    category = SynopsisCategory(app_label=app_label, local_identifier=local_identifier, name=name)
    SYNOPSIS_CATEGORIES[category.identifier] = category
    return category


def get_synopsis_category_choices():

    result = [(identifier, category.name + " [{}]".format(category.app_name.title()))
              for identifier, category in SYNOPSIS_CATEGORIES.items()]

    return result


class CuratedSynopsis(object):

    @property
    def synopsis(self):
        return self.synopsis_

    @property
    def prominence_css_class(self):
        return self.prominence_css_class_

    @prominence_css_class.setter
    def prominence_css_class(self, value):
        self.prominence_css_class_ = value

    @property
    def prominence_index(self):

        if self.prominence_index_ is None:
            return self.synopsis_.prominence_index

        return self.prominence_index_

    @prominence_index.setter
    def prominence_index(self, value):
        self.prominence_index_ = value

    @property
    def prominence_order(self):

        if self.prominence_order_ is None:
            return self.synopsis_.prominence_order

        return self.prominence_order_

    @prominence_order.setter
    def prominence_order(self, value):
        self.prominence_order_ = value

    def __getattr__(self, name):
        return getattr(self.synopsis_, name)

    def __init__(self, synopsis):
        self.synopsis_ = synopsis
        self.prominence_css_class_ = ''
        self.prominence_index_ = ''
        self.prominence_order_ = ''