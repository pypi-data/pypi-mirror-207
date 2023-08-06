
from urllib.parse import quote

from .auxiliaries import as_integer, apply_aspect_ratio, compute_focal_alignment, format_styles, \
    apply_fit_and_alignment_styles

from csskit.common import CSSUnits, CSSUnitValue

__all__ = ['render_content_in_responsive_cell']


def default_renderer(cell, content, dimensions, adjustments, alignment, attributes, layout_sizes):
    return "<div></div>"


def render_content_in_responsive_cell(content, intrinsic_dimensions, focal_point, cell, renderer, attributes=None,
                                      is_replaced_element=True):

    # Use the defined cell aspect ratio or the intrinsic aspect ratio of the content
    cell_aspect_ratio = cell.aspect_ratio if cell.use_aspect_ratio else intrinsic_dimensions

    default_alignment = cell.content_alignment

    # Compute the horizontal and vertical alignment factor from the intrinsic content dimensions and the focal point;
    # if no focal point is defined, use the alignment of the cell
    alignment = compute_focal_alignment(intrinsic_dimensions[0], intrinsic_dimensions[1], focal_point, default_alignment)

    # The default rendition dimensions are the intrinsic dimensions
    render_dimensions = intrinsic_dimensions
    adjustments = 0, 0, 0, 0

    if cell.content_fit is cell.FitCover:

        # Shrink the intrinsic dimensions to achieve the cell aspect ratio
        render_dimensions, adjustments = \
            apply_aspect_ratio(intrinsic_dimensions, cell_aspect_ratio, expand=False, alignment=alignment)

    # Copy any styles defined on the cell. They will be applied to the content element.

    styles = dict(cell.styles)

    if not is_replaced_element and cell.use_aspect_ratio and cell.content_fit is cell.FitContain:
        styles['--aspect-ratio'] = '{:d}/{:d}'.format(cell.aspect_ratio[0], cell.aspect_ratio[1])

    # Compute the setting for the object-position CSS property:

    # alignment = CSSUnitValue(value=alignment[0] * 100.0, unit=CSSUnits.PERCENTAGE_UNIT), \
    #             CSSUnitValue(value=alignment[1] * 100.0, unit=CSSUnits.PERCENTAGE_UNIT)

    # Express the content_fit and alignment settings as CSS properties
    # styles = apply_fit_and_alignment_styles(cell.content_fit, alignment, styles)

    extra_classes = []

    if cell.use_aspect_ratio and cell.content_fit is cell.FitContain:

        # We need to maintain the cell's aspect ratio if content_fit is contain.
        # A div wrapper with the desired aspect ratio allows us to scale the
        # the image appropriately.

        # extra_classes.append('fitted-aspect-ratio')
        pass

    # Format the element attributes

    attributes = dict(attributes) if attributes is not None else {}

    if styles:
        attributes['style'] = format_styles(styles)

    if cell.style_classes or extra_classes:
        attributes['class'] = cell.formatted_style_classes + " " + " ".join(extra_classes)

    sizes_list = []

    for condition, size in cell.conditional_sizes:
        sizes_list.append('({}) {}'.format(condition, size))

    sizes_list.append(str(cell.default_size))
    sizes_list = ', '.join(sizes_list)

    # Render the content
    result = renderer(cell, content, render_dimensions, adjustments, alignment, attributes, sizes_list)

    # We need to maintain the cell's aspect ratio if content_fit is contain and is_replaced_element is True.
    # A div wrapper with the desired aspect ratio is defined by using the padding "hack".

    if is_replaced_element and cell.use_aspect_ratio and cell.content_fit is cell.FitContain:

        # "position: relative; height: 0; padding-top: calc({:6f} * 100%);"

        result = '<div style="--aspect-ratio: {:d}/{:d};">{}</div>'.format(
                    cell.aspect_ratio[0], cell.aspect_ratio[1], result)

    return result
