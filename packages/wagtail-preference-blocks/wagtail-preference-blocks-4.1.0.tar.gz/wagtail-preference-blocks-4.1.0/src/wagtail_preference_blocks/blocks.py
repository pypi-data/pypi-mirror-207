import collections

from django.apps import apps
from django.core import checks

from wagtail import blocks

from wagtail_dynamic_choice.blocks import AlternateSnippetChooserBlock, DynamicMultipleChoiceBlock
from wagtail_dynamic_stream_block.blocks import DynamicStreamBlock, DynamicStreamValue

from wagtail_switch_block.block_registry import BlockRegistry
from wagtail_switch_block.blocks import DynamicSwitchBlock

from .apps import get_app_label

__all__ = ['BasePreferenceBlock', 'PreferencesBlock', 'PreferencesContextBlock', 'PreferencesValue',
           'preference_block_choices', 'register_preference_block',  # noqa
           'BLOCK_HINTS_VARIABLE', 'BaseHintBlock', 'BlockHintConsumerMixin',
           'block_hint_block_choices', 'register_block_hint_block',  # noqa
           ]

APP_LABEL = get_app_label()


class PreferenceBlockRegistry(BlockRegistry):

    # noinspection PyMethodMayBeStatic
    def should_register_block(self, app_label, local_identifier, block_type, block_args, block_kwargs, **kwargs):
        if not issubclass(block_type, BasePreferenceBlock):
            raise RuntimeError("Registered block type must be a subclass of BasePreferenceBlock")

        return True

    def instantiate_blocks_for_switch_block(self, switch_block):

        # This condition is important to get right:
        # The wagtail_switch_block app in its ready() method
        # calls update_dynamic_switch_blocks. At this point
        # apps.ready is False, but apps.apps_ready and apps.models_ready are True.
        # So checking apps.ready at this point would not update the dynamic switch blocks as expected.
        if not apps.apps_ready or not apps.models_ready:
            return []

        return super().instantiate_blocks_for_switch_block(switch_block)

    # noinspection PyMethodMayBeStatic
    def should_include_entry_for_switch_block(self, identifier, entry, switch_block):
        return True

    # noinspection PyMethodMayBeStatic
    def instantiate_block(self, identifier, entry, switch_block):

        block_kwargs = dict(entry.block_kwargs)
        block = entry.block_type(*entry.block_args, **block_kwargs)
        block.set_name(identifier)

        return block


REFERENCE_BLOCK_REGISTRY = PreferenceBlockRegistry()
REFERENCE_BLOCK_REGISTRY.define_procedures_in_caller_module("preference")


class BasePreferenceBlock(blocks.StructBlock):

    class Meta:
        min_num = 0
        max_num = 1
        category = None

    targets = DynamicMultipleChoiceBlock(
        choices_function_name=APP_LABEL + ".targets.preference_target_choices",
        required=False,
        default=[]
    )

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs


class ValueIndex:

    def __init__(self):
        self._values = []

    def append(self, value):
        self._values.append(value)

    def value(self):

        if not self._values:
            return None

        return self._values[-1]

    def values(self):
        return self._values


class TargetIndex:

    def __init__(self):
        self._index = collections.OrderedDict()

    def setdefault(self, target_name, default):
        return self._index.setdefault(target_name, default)

    def for_target(self, target_name=None):
        if not target_name:
            return self._index

        return self._index.get(target_name, ValueIndex())


class PreferenceIndex:

    def __init__(self, stream_values):
        self._index = None
        self._stream_values = list(stream_values)

    def _compute(self):

        self._index = collections.OrderedDict()

        for stream_value in self._stream_values:
            for child in stream_value:
                for target in child.value['targets']:
                    values_by_target = self._index.setdefault(child.block.name, TargetIndex())
                    values = values_by_target.setdefault(target, ValueIndex())
                    values.append(child.value)

    def __getitem__(self, preference_name):

        if self._index is None:
            self._compute()

        return self._index.get(preference_name, TargetIndex())


PreferencesValue = DynamicStreamValue


class PreferencesBlock(DynamicStreamBlock):

    class Meta:
        required = False
        template_variable = 'preferences'
        preference_blocks_function_name = APP_LABEL + ".blocks.preference_block_choices"
        block_counts = {}

    def __init__(self, **kwargs):

        preference_blocks_function_name = kwargs.pop('preference_blocks_function_name',
                                                     self._meta_class.preference_blocks_function_name) # noqa

        default_block_counts = kwargs.pop('block_counts',
                                   self._meta_class.block_counts) # noqa

        default_block_counts = dict(default_block_counts)

        super(PreferencesBlock, self).__init__(child_blocks_function_name=preference_blocks_function_name,
                                               preference_blocks_function_name=preference_blocks_function_name,
                                               default_block_counts=default_block_counts,
                                               block_counts={},
                                               **kwargs)

    def update_child_blocks(self):

        super().update_child_blocks()

        self.meta.block_counts.clear()
        self.meta.block_counts.update(self.meta.default_block_counts)

        for name, block in self.child_blocks.items():

            self.meta.block_counts[name] = {
                'min_num': block.meta.min_num,
                'max_num': block.meta.max_num
            }

    def check(self, **kwargs):
        errors = super().check(**kwargs)
        for name, child_block in self.child_blocks.items():

            if not isinstance(child_block, BasePreferenceBlock):

                errors.append(checks.Error(
                    "Block %r is invalid" % self.name,
                    hint="Blocks must be derived from BasePreferenceBlock",
                    obj=kwargs.get("field", self),
                    id="wagtail_preference_blocks.E001",
                ))

        return errors

    def render(self, value, context=None):

        if context:
            context[self.meta.template_variable] = value

        return ''


class PreferencesContext(blocks.StructValue):

    def __init__(self, *args, **kwargs):
        super(PreferencesContext, self).__init__(*args, **kwargs)

        stream_values = []

        for profile in self['profiles']:

            if not profile:
                continue

            stream_values.append(profile.preferences)

        local_stream_value = self.get('preferences', None)

        if local_stream_value:
            stream_values.append(local_stream_value)

        self.index = PreferenceIndex(stream_values)

    def by_name(self, preference_name=None):

        if not preference_name:
            return self.index

        return self.index[preference_name]


class PreferencesContextBlock(blocks.StructBlock):

    class Meta:
        value_class = PreferencesContext
        preference_blocks_function_name = APP_LABEL + ".blocks.preference_block_choices"
        block_counts = {}

    profiles = blocks.ListBlock(AlternateSnippetChooserBlock(
                                target_model=APP_LABEL + ".profile", required=True),
                                required=None,
                                default=[])

    def __init__(self, **kwargs):

        preference_blocks_function_name = kwargs.pop('preference_blocks_function_name',
                                                     self._meta_class.preference_blocks_function_name) # noqa

        block_counts = kwargs.pop('block_counts', self._meta_class.block_counts) # noqa

        if 'preferences' not in self.base_blocks:

            preferences_block = PreferencesBlock(preference_blocks_function_name=preference_blocks_function_name,
                                                 block_counts=block_counts)

            preferences_block.set_name('preferences')

            self.base_blocks['preferences'] = preferences_block

        super(PreferencesContextBlock, self).__init__(**kwargs)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs


LUMINOSITY_CHOICES = [('default', 'Default'),
                      ('light', 'Light'),
                      ('dark', 'Dark')]


class LuminosityBlock(BasePreferenceBlock):

    class Meta:
        category = 'Luminosity'

    value = blocks.ChoiceBlock(choices=LUMINOSITY_CHOICES, default=LUMINOSITY_CHOICES[0][0])

register_preference_block(APP_LABEL, 'luminosity', LuminosityBlock, [], {}) # noqa


SIZE_CHOICES = [('default', 'Default'),
                ('minimal', 'Minimal'),
                ('compact', 'Compact'),
                ('spacious', 'Spacious')]


class SizeBlock(BasePreferenceBlock):

    class Meta:
        category = 'Appearance'

    value = blocks.ChoiceBlock(choices=SIZE_CHOICES, default=SIZE_CHOICES[0][0])

register_preference_block(APP_LABEL, 'size', SizeBlock, [], {}) # noqa


class BlockHintIndex:

    def __init__(self):
        self._index = collections.OrderedDict()

    def __setitem__(self, block, value):

        values = self._index.setdefault(block.name, ValueIndex())
        values.append(value)

    def __getitem__(self, hint_name):
        return self._index.get(hint_name, ValueIndex())


class BlockHintRegistry(BlockRegistry):

    # noinspection PyMethodMayBeStatic
    def should_register_block(self, app_label, local_identifier, block_type, block_args, block_kwargs, **kwargs):
        if not issubclass(block_type, BaseHintBlock):
            raise RuntimeError("Registered block type must be a subclass of BaseHintBlock")

        return True

    def instantiate_blocks_for_switch_block(self, switch_block):

        # This condition is important to get right:
        # The wagtail_switch_block app in its ready() method
        # calls update_dynamic_switch_blocks. At this point
        # apps.ready is False, but apps.apps_ready and apps.models_ready are True.
        # So checking apps.ready at this point would not update the dynamic switch blocks as expected.
        if not apps.apps_ready or not apps.models_ready:
            return []

        return super().instantiate_blocks_for_switch_block(switch_block)

    # noinspection PyMethodMayBeStatic
    def should_include_entry_for_switch_block(self, identifier, entry, switch_block):
        return True

    # noinspection PyMethodMayBeStatic
    def instantiate_block(self, identifier, entry, switch_block):

        block_kwargs = dict(entry.block_kwargs)
        block = entry.block_type(*entry.block_args, **block_kwargs)
        block.set_name(identifier)

        return block


BLOCK_HINT_REGISTRY = BlockHintRegistry()
BLOCK_HINT_REGISTRY.define_procedures_in_caller_module("block_hint")


BLOCK_HINTS_VARIABLE = "__block_hints__"


class BaseHintBlock(blocks.StructBlock):

    class Meta:
        category = "Hints"

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs

    # noinspection PyMethodMayBeStatic
    def get_block_hints(self, context):
        return context[BLOCK_HINTS_VARIABLE]

    def render(self, value, context=None):

        if context is None:
            context = {}

        if BLOCK_HINTS_VARIABLE not in context:
            context[BLOCK_HINTS_VARIABLE] = BlockHintIndex()

        block_hints = self.get_block_hints(context)
        block_hints[self] = value

        return ''


class BlockHintConsumerMixin:

    # noinspection PyMethodMayBeStatic
    def get_block_hints(self, context):
        return context[BLOCK_HINTS_VARIABLE]

    def get_context(self, value, parent_context=None):

        context = super().get_context(value, parent_context) # noqa
        context['block_hints'] = self.get_block_hints(context)

        return context

    def render(self, value, context=None):

        if context is None:
            context = {}

        if BLOCK_HINTS_VARIABLE not in context:
            context[BLOCK_HINTS_VARIABLE] = BlockHintIndex()

        result = super().render(value, context=context) # noqa

        del context[BLOCK_HINTS_VARIABLE]

        return result

