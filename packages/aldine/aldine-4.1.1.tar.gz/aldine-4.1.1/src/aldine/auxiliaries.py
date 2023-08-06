
__all__ = ['apply_aspect_ratio', 'clip_value', 'compute_focal_alignment', 'format_numeric_value',
           'format_styles', 'apply_fit_and_alignment_styles', 'format_attributes']


def clip_value(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def compute_focal_alignment(width, height, focal_point, default_alignment=None):

    if focal_point:

        result = clip_value(focal_point[0] / width, 0.0, 1.0), \
                 clip_value(focal_point[1] / height, 0.0, 1.0)

    elif default_alignment:

        result = clip_value(default_alignment[0], 0.0, 1.0), \
                 clip_value(default_alignment[1], 0.0, 1.0)

    else:

        result = 0.5, 0.5

    return result


def apply_fit_and_alignment_styles(content_fit, content_alignment, styles=None):

    if styles is None:
        styles = {}

    if content_fit:
        styles['object-fit'] = content_fit.identifier

    if content_alignment:
        styles['object-position'] = "{} {}".format(content_alignment[0], content_alignment[1])

    return styles


def as_integer(operand):

    result = [0] * len(operand)

    for i in range(len(operand)):
        result[i] = int(round(operand[i]))

    result = tuple(result)
    return result


def apply_aspect_ratio(dimensions, aspect_ratio, expand=False, alignment=None, cast_to_integer=True):

    """
    Rescales the given dimensions to fit the provided aspect ratio. If expand is False,
    the dimensions will be shrunk along one axis, or expanded along one axis otherwise.
    The new dimensions will be returned together with a 4-tuple that indicates the change
    along each edge of a box defined by the old dimensions.

    :param dimensions: A 2-tuple of a width and a height
    :param aspect_ratio: A 2-tuple of a width and a height
    :param expand: If True, expand the dimensions along one axis, or shrink them along one axis if False.
    :param alignment: A numeric 2-tuple ([0..1], [0..1]) describing the relative alignment of the old dimensions relative to the new dimensions
    :param cast_to_integer: Cast all resulting values to integers.
    :return: A 4-tuple of top, right, bottom, left adjustments that when added to a box defined by
            the old dimensions produces a box defined by the new dimensions
    """

    x, y = aspect_ratio
    width, height = dimensions

    if alignment is None:
        alignment = 0.5, 0.5

    dx, dy = alignment
    dx, dy = clip_value(dx, 0.0, 1.0), clip_value(dy, 0.0, 1.0)

    aspect_ratio_number = x / y
    dimensions_ratio_number = width / height

    test = dimensions_ratio_number > aspect_ratio_number

    if test != expand:
        dimensions = aspect_ratio_number * height, height
        space = width - dimensions[0] if expand else dimensions[0] - width
        adjustments = 0, (1.0 - dx) * space, 0, dx * space
    elif dimensions_ratio_number == aspect_ratio_number:
        dimensions = width, height
        adjustments = 0, 0, 0, 0
    else:
        dimensions = width, width / aspect_ratio_number
        space = height - dimensions[1] if expand else dimensions[1] - height
        adjustments = dy * space, 0, (1.0 - dy) * space, 0

    if cast_to_integer:
        dimensions = as_integer(dimensions)
        adjustments = as_integer(adjustments)

    return dimensions, adjustments


def format_numeric_value(value, decimals=3):

    try:
        value = '{:d}'.format(value)
    except ValueError:
        f = '{{:.{:d}f}}'.format(decimals)
        value = f.format(value)

    return value


def format_styles(styles):

    result = []

    for key, value in styles.items():
        result.append("{}: {};".format(key, value))

    return " ".join(result)


def format_attributes(attributes):

    if not attributes:
        attributes = ''
    else:
        attributes = [name + '="' + value + '"' for name, value in attributes.items()]
        attributes = " ".join(attributes)

    return attributes
