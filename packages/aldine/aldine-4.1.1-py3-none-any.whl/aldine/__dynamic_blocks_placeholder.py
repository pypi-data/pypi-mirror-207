import copy

from django.utils.deconstruct import deconstructible
from steadfast import *

__all__ = ['Resolvable', 'ResponsiveDelegate']

SERIALISATION_PREFIX = "wagtail_dynamic_blocks."


@decl_serializable(
    SaveInitArguments(),
    type_identifier=SERIALISATION_PREFIX + 'resolvable'  # noqa
)
class Resolvable(object):

    def __init__(self):
        pass

    def save_init_arguments(self, arguments):
        pass

    def copy(self):
        return copy.deepcopy(self)

    def resolve(self, context, strict=False, cacheable=False, variables=None):
        return self


@deconstructible
class ResponsiveDelegate:

    def render_in_responsive_cell(self, item, cell, template_context=None):
        return ''
