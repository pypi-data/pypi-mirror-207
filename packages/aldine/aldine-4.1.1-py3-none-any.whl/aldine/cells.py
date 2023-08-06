import weakref
import types

from typing import Optional, Union

from steadfast import *

from csskit.common import CSSUnits, CSSUnitValue, CSSMathExpr, CSSObjectFitType, CSSObjectFitNone, \
    CSSObjectFitFill, CSSObjectFitCover, CSSObjectFitContain

from .auxiliaries import format_numeric_value, format_styles
from .apps import get_app_label
from .__dynamic_blocks_placeholder import Resolvable

__all__ = ['Cell', 'ResponsiveCell']

APP_LABEL = get_app_label()


class Cell:

    ContentFitType = CSSObjectFitType

    FitNone = CSSObjectFitNone
    FitContain = CSSObjectFitContain
    FitCover = CSSObjectFitCover
    FitFill = CSSObjectFitFill

    @property
    def render_index(self):
        return self.__render_index

    @property
    def source_order(self):
        return self.__source_order

    @property
    def default_size(self) -> Optional[Union[CSSUnitValue, CSSMathExpr]]:
        return self.__default_size

    @property
    def conditional_sizes(self):
        return self.__conditional_sizes[:] if isinstance(self.__conditional_sizes, list) else self.__conditional_sizes

    @property
    def use_aspect_ratio(self):
        return self.__aspect_ratio is not None

    @property
    def aspect_ratio(self):
        return self.__aspect_ratio

    @property
    def aspect_ratio_number(self):

        if not self.use_aspect_ratio:
            return None

        return self.__aspect_ratio[0] / self.__aspect_ratio[1]

    @property
    def aspect_ratio_as_text(self):

        if not self.use_aspect_ratio:
            return "1/1"

        return format_numeric_value(self.__aspect_ratio[0]) + "/" + \
               format_numeric_value(self.__aspect_ratio[1])

    @property
    def content_fit(self) -> ContentFitType:
        return self.__content_fit

    @property
    def content_alignment(self):
        return self.__content_alignment

    @property
    def styles(self):
        return self.__styles

    @property
    def formatted_styles(self):
        return format_styles(self.__styles)

    @property
    def style_classes(self):
        return self.__style_classes

    @property
    def formatted_style_classes(self):
        return " ".join(self.style_classes)

    @property
    def annotations(self):
        return self.__annotations

    @property
    def image_filter_expr(self):
        return self.__image_filter_expr

    def __init__(self, *,
                 render_index=0,
                 source_order=0,
                 default_size=None,
                 conditional_sizes=None,
                 aspect_ratio=None,
                 content_fit=None,
                 content_alignment=None,
                 styles=None,
                 style_classes=None,
                 annotations=None,
                 image_filter_expr=None):

        if conditional_sizes is None:
            conditional_sizes = []

        if isinstance(content_fit, str):
            content_fit = self.ContentFitType.from_identifier(content_fit)

        if content_fit is None:
            content_fit = self.FitCover

        if styles is None:
            styles = {}

        if style_classes is None:
            style_classes = []

        if annotations is None:
            annotations = {}

        if isinstance(annotations, dict):
            annotations = types.SimpleNamespace(**annotations)

        if not isinstance(annotations, types.SimpleNamespace):
            raise RuntimeError("annotations argument must be a dict or SimpleNamespace")

        self.__render_index = render_index
        self.__source_order = source_order

        self.__default_size = default_size
        self.__conditional_sizes = conditional_sizes \
            if isinstance(conditional_sizes, Resolvable) else \
            list(conditional_sizes)

        self.__aspect_ratio = aspect_ratio
        self.__content_fit = content_fit
        self.__content_alignment = content_alignment
        self.__styles = dict(styles)
        self.__style_classes = list(style_classes)

        self.__annotations = types.SimpleNamespace(**annotations.__dict__)
        self.__image_filter_expr = image_filter_expr


@decl_serializable(
    SaveInitArguments(),
    type_identifier=APP_LABEL + '.cell'  # noqa
)
class ResponsiveCell(Cell, Resolvable):

    @property
    def context(self):
        return self.__context_ref() if self.__context_ref else None

    @context.setter
    def context(self, value):
        self.__context_ref = weakref.ref(value) if value else None

    @property
    def media_conditions(self):
        return list(self.__definitions_by_media_condition.keys())

    def __init__(self, *,
                 render_index=0, source_order=0,
                 default_size=None, conditional_sizes=None,
                 aspect_ratio=None,
                 content_fit=None, content_alignment=None,
                 styles=None, style_classes=None,
                 annotations=None,
                 image_filter_expr=None,
                 cells_by_media_condition=None):

        Cell.__init__(self,
                      render_index=render_index, source_order=source_order,
                      default_size=default_size, conditional_sizes=conditional_sizes,
                      aspect_ratio=aspect_ratio,
                      content_fit=content_fit, content_alignment=content_alignment,
                      styles=styles,
                      style_classes=style_classes,
                      annotations=annotations,
                      image_filter_expr=image_filter_expr)

        Resolvable.__init__(self)

        if cells_by_media_condition is None:
            cells_by_media_condition = []

        self.__context_ref = None
        self.__cells_by_media_condition = list(cells_by_media_condition)
        self.__cells_dict = {}

        for condition, cell in cells_by_media_condition:
            self.__cells_dict[condition] = cell

    def save_init_arguments(self, arguments):

        arguments.render_index = self.render_index
        arguments.source_order = self.source_order
        arguments.default_size = self.default_size

        arguments.conditional_sizes = self.conditional_sizes \
            if isinstance(self.conditional_sizes, Resolvable) else \
            list(self.conditional_sizes)

        arguments.aspect_ratio = self.aspect_ratio
        arguments.content_fit = self.content_fit
        arguments.content_alignment = self.content_alignment
        arguments.styles = dict(self.styles)
        arguments.style_classes = list(self.style_classes)
        arguments.annotations = dict(self.annotations.__dict__)
        arguments.cells_by_media_condition = list(self.__cells_by_media_condition)

    def cell_for_media_condition(self, media_condition) -> Optional[Cell]:

        result = self.__cells_dict.get(media_condition, None)

        if result is None:
            return self

        return result

    def resolve(self, context, strict=False, cacheable=False, variables=None):

        args = types.SimpleNamespace()
        self.save_init_arguments(args)

        if isinstance(args.render_index, Resolvable):
            args.render_index = args.render_index.resolve(context, strict, cacheable, variables)

        if isinstance(args.source_order, Resolvable):
            args.source_order = args.source_order.resolve(context, strict, cacheable, variables)

        if isinstance(args.default_size, Resolvable):
            args.default_size = args.default_size.resolve(context, strict, cacheable, variables)

        if isinstance(args.conditional_sizes, Resolvable):
            args.conditional_sizes = args.conditional_sizes.resolve(context, strict, cacheable, variables)

        for index, item in enumerate(args.conditional_sizes):

            if isinstance(item, Resolvable):
                item = item.resolve(context, strict, cacheable, variables)
                args.conditional_sizes[index] = item
                continue

            condition, value = item

            if isinstance(value, Resolvable):
                value = value.resolve(context, strict, cacheable, variables)

            args.conditional_sizes[index] = condition, value

        if isinstance(args.aspect_ratio, Resolvable):
            args.aspect_ratio = args.aspect_ratio.resolve(context, strict, cacheable, variables)

        if isinstance(args.content_fit, Resolvable):
            args.content_fit = args.content_fit.resolve(context, strict, cacheable, variables)

        if isinstance(args.content_alignment, Resolvable):
            args.content_alignment = args.content_alignment.resolve(context, strict, cacheable, variables)

        for key, value in self.styles.items():

            if isinstance(value, Resolvable):
                value = value.resolve(context, strict, cacheable, variables)

            args.styles[key] = value

        for index, value in enumerate(args.style_classes):

            if isinstance(value, Resolvable):
                value = value.resolve(context, strict, cacheable, variables)

            args.style_classes[index] = value

        for index, cell in enumerate(args.cells_by_media_condition):
            cell = cell.resolve(context, strict, cacheable, variables)
            args.cells_by_media_condition[index] = cell

        for name, value in self.annotations.__dict__.items():

            if isinstance(value, Resolvable):
                value = value.resolve(context, None, cacheable, variables)

            args.annotations[name] = value

        args.image_filter_expr = self.image_filter_expr

        return self.__class__(**args.__dict__)

