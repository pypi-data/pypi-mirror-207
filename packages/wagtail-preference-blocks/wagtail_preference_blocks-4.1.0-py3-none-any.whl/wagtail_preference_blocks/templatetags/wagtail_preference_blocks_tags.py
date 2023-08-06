
from django import template

from wagtail.templatetags.wagtailcore_tags import include_block as standard_include_block


from ..apps import get_app_label
from ..blocks import BLOCK_HINTS_VARIABLE


APP_LABEL = get_app_label()

register = template.Library()


class ValueProxy:

    def __init__(self, value, context):
        self.value = value
        self.context = context

    def render_as_block(self, context=None):

        if hasattr(self.value, "render_as_block"):

            result = self.value.render_as_block(context=context)

            if BLOCK_HINTS_VARIABLE in context:
                self.context[BLOCK_HINTS_VARIABLE] = context[BLOCK_HINTS_VARIABLE]
            elif BLOCK_HINTS_VARIABLE in self.context:
                del self.context[BLOCK_HINTS_VARIABLE]

            return result
        else:
            return self.value


class ValueInterceptor:

    def __init__(self, fe):
        self.fe = fe

    def resolve(self, context):
        value = self.fe.resolve(context)
        value = ValueProxy(value, context)
        return value


@register.tag
def include_block_with_hints(parser, token):

    node = standard_include_block(parser, token)

    if hasattr(node, 'block_var'):
        setattr(node, 'block_var', ValueInterceptor(node.block_var))

    return node
