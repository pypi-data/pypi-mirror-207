from types import SimpleNamespace

from wagtail_content_admin.blocks import BaseContentRenderBlock

from .apps import get_app_label
from .cells import ResponsiveCell

__all__ = ['BaseContentLayoutBlock']


APP_LABEL = get_app_label()


class BaseContentLayoutBlock(BaseContentRenderBlock):

    class Meta:

        icon = "placeholder"

        cells_and_items_var = "cells_and_items"

    # noinspection PyMethodMayBeStatic
    def create_cell_state(self, value, context):
        return SimpleNamespace()

    # noinspection PyMethodMayBeStatic
    def create_cell_for_item(self, item, render_index, source_index, annotations, cell_state):
        cell = ResponsiveCell(
            render_index=render_index,
            source_order=source_index,
            annotations=annotations
        )

        return cell

    def contribute_content_to_context(self, value, content, context):

        super(BaseContentLayoutBlock, self).contribute_content_to_context(value, content, context)

        cell_state = self.create_cell_state(value, context)
        cells_and_items = []

        for index, entry in enumerate(zip(content.items, content.annotations) if content.items else []):
            item, item_annotations = entry

            cell = self.create_cell_for_item(item, index, index, item_annotations, cell_state)
            cells_and_items.append((cell, item))

        if self.meta.cells_and_items_var:
            context[self.meta.cells_and_items_var] = cells_and_items
