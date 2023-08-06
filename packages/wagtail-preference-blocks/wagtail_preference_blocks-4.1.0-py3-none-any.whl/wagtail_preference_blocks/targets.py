from django.apps import apps
from .apps import get_app_label

__all__ = ['PreferenceTarget', 'preference_target_choices']

APP_LABEL = get_app_label()


class PreferenceTarget:

    __REGISTRY = {}

    @property
    def identifier(self):
        return self.app_label + "_" + self.local_identifier

    def __init__(self, app_label, local_identifier, name):

        self.app_label = app_label
        self.local_identifier = local_identifier
        self.name = name

        app = apps.get_app_config(self.app_label)
        self.app_name = app.verbose_name
        self.__class__.__REGISTRY[self.identifier] = self

    @classmethod
    def all(cls):
        return list(cls.__REGISTRY.values())


def preference_target_choices():

    return [(target.identifier, target.name) for target in PreferenceTarget.all()]

