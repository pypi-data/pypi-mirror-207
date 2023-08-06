from django.apps import apps
from django.utils.html import format_html_join, mark_safe

from wagtail import blocks
from wagtail_switch_block.blocks import SwitchBlock, SwitchValue

from csskit.common import CSSUnits
from csskit.blocks import CSSUnitValueBlock, ComplexCSSUnitValueBlock, CSSGapBlock

from .apps import get_app_label

__all__ = ['BeginColumnsBlock', 'EndColumnsBlock', 'HeadingBlock']

APP_LABEL = get_app_label()


class ColumnsSpecifierValue(SwitchValue):

    @property
    def as_common_value(self):

        if self.type == 'count':
            return self.value

        return self.value.as_common_value


class ColumnsSpecifierBlock(SwitchBlock):

    count = blocks.IntegerBlock(min_value=1)
    width = ComplexCSSUnitValueBlock()

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


class BeginColumnsBlock(blocks.StructBlock):
    class Meta:
        verbose_name = "Begin Columns"
        template = APP_LABEL + "/blocks/begin_columns_block.html"
        class_names = "as-columns"
        group = "Layout"

    columns = ColumnsSpecifierBlock()
    row_gap = CSSGapBlock()
    column_gap = CSSGapBlock()

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


class EndColumnsBlock(blocks.StaticBlock):

    class Meta:
        verbose_name = "End Columns"
        template = APP_LABEL + "/blocks/end_columns_block.html"
        group = "Layout"

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


class ColumnBreakBlock(blocks.StaticBlock):

    class Meta:
        verbose_name = "Column Break"
        template = APP_LABEL + "/blocks/column_break_block.html"
        group = "Layout"

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


class BeginFlowBlock(blocks.StructBlock):
    class Meta:
        verbose_name = "Begin Flow"
        template = APP_LABEL + "/blocks/begin_flow_block.html"
        class_names = "as-flow"
        group = "Layout"

    direction = blocks.ChoiceBlock(choices=[('row', 'Row'), ('row-reverse', 'Reverse Row'),
                                            ('column', 'Column'), ('column-reverse', 'Reverse Row')],
                                   default="row")

    wrap = blocks.BooleanBlock(default=False, required=False)

    row_gap = CSSGapBlock()
    column_gap = CSSGapBlock()

    min_item_width = ComplexCSSUnitValueBlock(choices=('value', 'undefined'),
                                              default_block_name='undefined',
                                              label="Minimum Item Width")

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


class EndFlowBlock(blocks.StaticBlock):

    class Meta:
        verbose_name = "End Flow"
        template = APP_LABEL + "/blocks/end_flow_block.html"
        group = "Layout"

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


class FlowBreakBlock(blocks.StaticBlock):

    class Meta:
        verbose_name = "Flow Break"
        template = APP_LABEL + "/blocks/flow_break_block.html"
        group = "Layout"

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


have_anchor_support = None
current_anchor_registry_and_inventory = None


def import_anchor_support():

    global have_anchor_support
    global current_anchor_registry_and_inventory

    if have_anchor_support is None:

        have_anchor_support = False

        if apps.is_installed('bon_voyage'):

            try:

                from bon_voyage.anchors import current_anchor_registry_and_inventory
                have_anchor_support = True

            except ImportError:
                have_anchor_support = False

    return have_anchor_support


def define_anchor(anchor_category, anchor_identifier, level):

    if not import_anchor_support():
        return ''

    registry, inventory = current_anchor_registry_and_inventory() # noqa

    if not registry:
        return ''

    result = registry.define_anchor(inventory, anchor_category, anchor_identifier, level)
    return result


def label_anchor(anchor_category, anchor_identifier, label_format='no_prefix_label'):

    if not import_anchor_support():
        return ''

    registry, inventory = current_anchor_registry_and_inventory() # noqa

    if not registry:
        return ''

    result = registry.label_anchor(inventory, anchor_category, anchor_identifier, label_format=label_format)
    return result


class HeadingBlock(blocks.StructBlock):

    class Meta:
        icon = 'form'
        template = APP_LABEL + '/blocks/heading_block.html'
        anchor_category = "section"

    heading = blocks.CharBlock(label="Heading", required=True, default="")
    level = blocks.ChoiceBlock(label="Level", required=True,
                               choices=[(i, "Level {:d}".format(i)) for i in range(1, 7)], default=2)

    anchor_identifier = blocks.CharBlock(label="Anchor Identifier", required=False)
    show_anchor_label = blocks.BooleanBlock(label="Show Anchor Label", required=False)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs

    def get_context(self, value, parent_context=None):

        context = super().get_context(value, parent_context)
        anchor_identifier = value['anchor_identifier']
        level = int(value['level'])

        if anchor_identifier:

            level = 0 if level < 2 else level - 2

            context['anchor_id'] = define_anchor(self.meta.anchor_category, anchor_identifier, level)

            if value['show_anchor_label']:
                context['anchor_label'] = label_anchor(self.meta.anchor_category, anchor_identifier)
            else:
                context['anchor_label'] = ''

        return context
