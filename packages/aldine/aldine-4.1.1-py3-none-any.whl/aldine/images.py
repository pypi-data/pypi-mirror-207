import bisect

from types import SimpleNamespace
from urllib.parse import quote

from .auxiliaries import as_integer, format_attributes, apply_fit_and_alignment_styles, format_styles

from .render import render_content_in_responsive_cell

from csskit.common import CSSUnits, CSSUnitValue

__all__ = ['ImageCurator', 'render_image_in_responsive_cell']

LANDSCAPE_RESOLUTIONS = [240, 320, 410, 640, 800, 1024, 1366, 1600, 2560, 3840, 5120, 7680]
PORTRAIT_RESOLUTIONS = [320, 480, 768, 900, 1200, 1440, 2160, 2880, 4320]


class ImageCurator(object):

    def __init__(self):
        self.__resolutions = SimpleNamespace()
        self.__resolutions.landscape = LANDSCAPE_RESOLUTIONS
        self.__resolutions.portrait = PORTRAIT_RESOLUTIONS

    def select_resolutions(self, dimensions):

        width, height = dimensions

        if width > height:
            resolutions = self.__resolutions.landscape
            value = width
            other_value = height

            def scaled_dimensions(value, other_value):
                return value, other_value

        else:
            resolutions = self.__resolutions.portrait
            value = height
            other_value = width

            def scaled_dimensions(value, other_value):
                return other_value, value

        index = bisect.bisect_left(resolutions, value)
        selected_resolutions = resolutions[:index]

        result = []

        for scaled_value in selected_resolutions:
            scaled_other_value = other_value * scaled_value / value
            result.append(scaled_dimensions(scaled_value, scaled_other_value))

        result.append(scaled_dimensions(value, other_value))
        return result


def render_img_tag(cell, content, dimensions, adjustments, alignment, attributes, layout_sizes, *, curator):

    image = content

    alignment = CSSUnitValue(value=alignment[0] * 100.0, unit=CSSUnits.PERCENTAGE_UNIT), \
                CSSUnitValue(value=alignment[1] * 100.0, unit=CSSUnits.PERCENTAGE_UNIT)

    # Express the content_fit and alignment settings as CSS properties
    alignment_styles = apply_fit_and_alignment_styles(cell.content_fit, alignment)
    alignment_styles = format_styles(alignment_styles)

    styles = attributes.get('style', '')

    if styles:
        styles += ' '

    attributes['style'] = styles + alignment_styles

    attributes = format_attributes(attributes)

    # Compute the rendition sizes based on the (computed) rendition dimensions
    rendition_sizes = [as_integer(size) for size in curator.select_resolutions(dimensions)]

    # Render the content in the selected rendition sizes

    renditions = []
    source_set = []

    for index, size in enumerate(rendition_sizes):
        rendition_filter = 'fill-{:d}x{:d}'.format(size[0], size[1])

        if cell.image_filter_expr:
            rendition_filter += "|" + cell.image_filter_expr

        rendition = image.get_rendition(rendition_filter)
        source_set.append('{} {:d}w'.format(quote(rendition.url), size[0]))
        renditions.append(rendition)

    base_url = renditions[-1].url

    result = '<img srcset="{}" sizes="{}" src="{}" alt="{}"{}>'.format(
        ', '.join(source_set), layout_sizes, quote(base_url), image.default_alt_text,
        attributes
    )

    return result


def render_image_in_responsive_cell(image, cell, curator, attributes=None):

    image_dimensions = image.width, image.height

    return render_content_in_responsive_cell(
        image, image_dimensions, image.get_focal_point(), cell,
        lambda *args: render_img_tag(*args, curator=curator),
        attributes=attributes)
