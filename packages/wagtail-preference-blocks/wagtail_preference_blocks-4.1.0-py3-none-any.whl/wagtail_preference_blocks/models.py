from django.db import models as django_models

from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import MultiFieldPanel, FieldPanel

from django_auxiliaries.validators import python_identifier_validator
from wagtail_block_model_field.fields import BlockModelField

from .blocks import PreferencesBlock, PreferencesValue

__all__ = ['Profile']


@register_snippet
class Profile(django_models.Model):

    class Meta:
        constraints = [
            django_models.UniqueConstraint(fields=['identifier'], name='unique_%(app_label)s_%(class)s.identifier')
        ]

    identifier = django_models.CharField(max_length=128, default='', validators=[python_identifier_validator])
    description = django_models.CharField(max_length=255, default='')

    preferences = BlockModelField(PreferencesBlock(), value_class=PreferencesValue)

    panels = [
        MultiFieldPanel(
            [FieldPanel('identifier'),
             FieldPanel('description')
            ],

            heading="General"
        ),

        FieldPanel('preferences')
    ]

    def __str__(self):
        return self.description + " [{}]".format(self.identifier) # noqa