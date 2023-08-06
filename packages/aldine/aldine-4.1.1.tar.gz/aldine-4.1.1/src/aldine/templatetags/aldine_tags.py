from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.templatetags.static import static

from ..cells import Cell, ResponsiveCell
from ..apps import get_app_label

APP_LABEL = get_app_label()

register = template.Library()


@register.simple_tag(name="render_responsive_cell", takes_context=True)
def render_responsive_cell_tag(context, responsive_delegate, cell, *, item=None):

    if not responsive_delegate:
        return ''

    if item is None:

        if cell.context is None:
            return ''

        item = cell.context.items[cell.source_order]

    result = responsive_delegate.render_in_responsive_cell(item, cell, template_context=context)
    result = mark_safe(result)
    return result


@register.simple_tag(name="define_cell")
def define_cell_tag(*,
                    render_index=0,
                    source_order=0,
                    default_size=None,
                    conditional_sizes=None,
                    aspect_ratio=None,
                    content_fit=None,
                    content_alignment=None,
                    styles=None,
                    style_classes=None,
                    annotations=None):

    result = Cell(render_index=render_index,
                  source_order=source_order,
                  default_size=default_size,
                  conditional_sizes=conditional_sizes,
                  aspect_ratio=aspect_ratio,
                  content_fit=content_fit,
                  content_alignment=content_alignment,
                  styles=styles,
                  style_classes=style_classes,
                  annotations=annotations)

    return result


@register.simple_tag(name="define_responsive_cell")
def define_responsive_cell_tag(responsive_context, *,
                               render_index=0,
                               source_order=0,
                               default_size=None,
                               conditional_sizes=None,
                               aspect_ratio=None,
                               content_fit=None,
                               content_alignment=None,
                               styles=None,
                               style_classes=None,
                               annotations=None):

    result = ResponsiveCell(render_index=render_index,
                            source_order=source_order,
                            default_size=default_size,
                            conditional_sizes=conditional_sizes,
                            aspect_ratio=aspect_ratio,
                            content_fit=content_fit,
                            content_alignment=content_alignment,
                            styles=styles,
                            style_classes=style_classes,
                            annotations=annotations)

    result.context = responsive_context
    return result


@register.simple_tag(takes_context=False)
def aldine_support(*, container_element):

    if container_element == 'head':
        return format_html('<link rel="stylesheet" type="text/css" href="{}">',
                           static(APP_LABEL + '/css/aldine.css'))

    return ''

