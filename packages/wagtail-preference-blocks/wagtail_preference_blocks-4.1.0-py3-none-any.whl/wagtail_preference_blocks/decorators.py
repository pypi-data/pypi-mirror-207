from wagtail.admin.panels import FieldPanel

from wagtail_block_model_field.fields import BlockModelField

from .blocks import PreferencesContextBlock, PreferencesContext


__all__ = 'provides_preferences_context'


def provides_preferences_context(cls):

    preferences_context = BlockModelField(PreferencesContextBlock(label="Preferences Context"),
                                          value_class=PreferencesContext,
                                          verbose_name="Preferences")

    preferences_context.contribute_to_class(cls, name="preferences_context")

    panel = FieldPanel('preferences_context')

    if hasattr(cls, 'content_panels'):
        cls.content_panels.extend([panel])
    elif hasattr(cls, 'panels'):
        cls.panels.extend([panel])

    return cls

