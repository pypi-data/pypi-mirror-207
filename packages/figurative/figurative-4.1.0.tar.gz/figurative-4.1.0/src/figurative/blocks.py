from types import SimpleNamespace

from wagtail import blocks

from csskit.common import CSSTextAlignment, CSSUnitValue, CSSUnits
from csskit.blocks import CSSObjectPositionBlock, CSSEdgesBlock

from media_catalogue.layout_blocks import MediaItemLayoutBlock

from wagtail_dynamic_choice.blocks import AlternateSnippetChooserBlock
from wagtail_preference_blocks.blocks import BaseHintBlock, register_block_hint_block, BlockHintConsumerMixin

from tour_guide.anchors import current_anchor_registry_and_inventory
from tour_guide.blocks import RichLinkBlock
from aldine.cells import ResponsiveCell

from .apps import get_app_label

__all__ = ['FigureBlock', 'SlideshowBlock']

APP_LABEL = get_app_label()


class OverlayCaptionPlacementHint(BaseHintBlock):

    choices = [
        ('default', 'Default'),
        ('compact', 'Compact'),
    ]

    value = blocks.ChoiceBlock(label='Value', choices=choices, default=choices[0][0])


OVERLAY_CAPTION_PLACEMENT_HINT = \
    register_block_hint_block(APP_LABEL, 'overlay_caption_placement', OverlayCaptionPlacementHint, [], {}) # noqa


ANNOTATION_LINK_BLOCK = RichLinkBlock()
ANNOTATION_LINK_BLOCK.set_name('link')


class FigureBlock(BlockHintConsumerMixin, MediaItemLayoutBlock):

    arrangement_choices = [
        ('one-column', 'Single Column'),
        ('two-columns', 'Two Columns'),
        ('three-columns', 'Three Columns'),
        ('four-columns', 'Four Columns'),
        ('five-columns', 'Five Columns'),
    ]

    format_choices = [
        ('square', '1:1'),

        ('landscape-2-1', '2:1'),
        ('landscape-3-2', '3:2'),
        ('landscape-4-3', '4:3'),
        ('landscape-16-10', '16:10'),
        ('landscape-16-9', '16:9'),
        ('landscape-21-9', '21:9'),

        ('portrait-1-2', '1:2'),
        ('portrait-2-3', '2:3'),
        ('portrait-3-4', '3:4'),
        ('portrait-10-16', '10:16'),
        ('portrait-9-16', '9:16'),
        ('portrait-9-21', '9:21'),

        ('viewport', 'Viewport')
    ]

    fit_width_choices = [
        ('container', 'Text/Container Width'),
        ('viewport', 'Viewport Width')
    ]

    content_fit_choices = [
        ('cover', 'Cover'),
        ('contain', 'Contain'),
        ('fill', 'Fill'),
    ]

    level_choices = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
    ]

    text_alignment_choices = CSSTextAlignment.choices()

    root_element_css_classes = {
        'one-column': 'panels-1-col',
        'two-columns': 'panels-2-col',
        'three-columns': 'panels-3-col',
        'four-columns': 'panels-4-col',
        'five-columns': 'panels-5-col',
        'slideshow': 'slideshow',
    }

    class Meta:

        icon = "placeholder"
        template = APP_LABEL + "/blocks/figure_block.html"
        scale_factor = 1.0
        caption_label_css_class = "anchor-label"
        figure_css_class = ""
        default_anchor_category = "figure"

    arrange_as = blocks.ChoiceBlock(label='Arrange As', choices=arrangement_choices, default=arrangement_choices[0][0])
    fit_width = blocks.ChoiceBlock(label='Fit Width', choices=fit_width_choices, default=fit_width_choices[0][0])
    format = blocks.ChoiceBlock(label='Format', choices=format_choices, default=format_choices[0][0])

    content_fit = blocks.ChoiceBlock(label='Content Fit', choices=content_fit_choices, default=content_fit_choices[0][0])
    content_alignment = CSSObjectPositionBlock(label='Content Alignment',
                                               accepted_css_units=[
                                                (CSSUnits.PERCENTAGE_UNIT_IDENTIFIER, CSSUnits.PERCENTAGE_UNIT_LABEL)])
    padding = CSSEdgesBlock(label='Padding')

    caption = blocks.CharBlock(label="Caption", default='', required=False)
    show_captions = blocks.BooleanBlock(label='Show Captions', default=False, required=False)
    caption_alignment = blocks.ChoiceBlock(label='Align Caption',
                                           choices=text_alignment_choices, default=text_alignment_choices[0][0])

    # anchor_category = AlternateSnippetChooserBlock(target_model="tour_guide.anchorcategorysetting", # noqa
    #                                                use_identifier_as_value=True, default="figure", required=False)

    anchor_level = blocks.ChoiceBlock(identifier='anchor_level', label='Anchor Level', choices=level_choices,
                                      default=level_choices[0][0])

    image_filter_expr = blocks.CharBlock(label="Image Filter Expression", default='', required=False)

    def __init__(self, *args, **kwargs):

        default_anchor_category = kwargs.pop('default_anchor_category', self._meta_class.default_anchor_category) # noqa

        anchor_category = AlternateSnippetChooserBlock(
                                target_model="tour_guide.anchorcategorysetting", # noqa
                                use_identifier_as_value=True, required=False, default=default_anchor_category)

        anchor_category.set_name('anchor_category')

        self.base_blocks['anchor_category'] = anchor_category

        super(FigureBlock, self).__init__(*args, default_anchor_category=default_anchor_category, **kwargs)

    # noinspection PyMethodMayBeStatic
    def compute_aspect_ratio(self, value, context):
        format_specifier = value.get('format', None)

        if format_specifier is None:
            return None

        if format_specifier == 'square':
            return 1, 1
        elif format_specifier.startswith('landscape-'):
            format_specifier = format_specifier[10:]
        elif format_specifier.startswith('portrait-'):
            format_specifier = format_specifier[9:]
        else:
            format_specifier = None

        if format_specifier is None:
            return None

        h, v = format_specifier.split('-')
        return int(h), int(v)

    # noinspection PyMethodMayBeStatic
    def compute_content_fit(self, value, context):
        content_fit = value.get('content_fit', None)

        if content_fit is None:
            return None

        content_fit = ResponsiveCell.ContentFitType.from_identifier(content_fit)
        return content_fit

    # noinspection PyMethodMayBeStatic
    def compute_content_alignment(self, value, context):
        alignment = value.get('content_alignment', None)

        if alignment is None:
            return None

        result = alignment.as_common_value

        if result.x is None and result.y is None:
            return None

        if result.x is None:
            return 0.5, result.y.value / 100.0  # CSSObjectPosition(x=CSSUnitValue(0), y=result.y)

        if result.y is None:
            return result.x.value / 100.0, 0.5  # CSSObjectPosition(x=result.x, y=CSSUnitValue(0))

        return result.x.value / 100.0, result.y.value / 100.0

    # noinspection PyMethodMayBeStatic
    def compute_padding(self, value, context):
        padding = value.get('padding', None)

        if padding is None:
            return None

        result = padding.as_common_value

        if result.top is None and result.left is None and result.bottom is None and result.right is None:
            return None

        return result

    # noinspection PyMethodMayBeStatic
    def compute_caption_alignment(self, value, context):
        alignment = value.get('caption_alignment', None)

        if not alignment:
            return None

        alignment = CSSTextAlignment.map_identifier_to_value(alignment)
        return alignment

    def compute_scale_factor(self, value, context):
        return context.get('scale_factor', None) or self.meta.scale_factor

    def compute_default_cell_size(self, value, context):

        scale_factor = self.compute_scale_factor(value, context)
        arrange_as = value.get('arrange_as', None)

        result = None

        if arrange_as == 'one-column':
            result = CSSUnitValue(100.0 * scale_factor, CSSUnits.VIEW_WIDTH_UNIT)
        elif arrange_as == 'two-columns':
            result = CSSUnitValue(50.0 * scale_factor, CSSUnits.VIEW_WIDTH_UNIT)
        elif arrange_as == 'three-columns':
            result = CSSUnitValue(100.0 / 3.0 * scale_factor, CSSUnits.VIEW_WIDTH_UNIT)
        elif arrange_as == 'four-columns':
            result = CSSUnitValue(25.0 * scale_factor, CSSUnits.VIEW_WIDTH_UNIT)
        elif arrange_as == 'five-columns':
            result = CSSUnitValue(20.0 * scale_factor, CSSUnits.VIEW_WIDTH_UNIT)

        return result

    def compute_conditional_cell_sizes(self, value, context):

        MAX_WIDTH_409PX = "max-width: 409px"
        MAX_WIDTH_639PX = "max-width: 639px"
        MAX_WIDTH_1023PX = "max-width: 1023px"
        MAX_WIDTH_1599PX = "max-width: 1599px"

        scale_factor = self.compute_scale_factor(value, context)
        arrange_as = value.get('arrange_as', None)

        viewport_width = CSSUnitValue(100.0 * scale_factor, CSSUnits.VIEW_WIDTH_UNIT)
        half_width = CSSUnitValue(50.0 * scale_factor, CSSUnits.VIEW_WIDTH_UNIT)
        result = None

        if arrange_as == 'one-column':
            result = [(MAX_WIDTH_409PX, viewport_width)]
        elif arrange_as == 'two-columns':
            result = [(MAX_WIDTH_639PX, viewport_width)]
        elif arrange_as == 'three-columns':
            result = [(MAX_WIDTH_639PX, viewport_width)]
        elif arrange_as == 'four-columns':
            result = [(MAX_WIDTH_639PX, viewport_width), (MAX_WIDTH_1023PX, half_width)]
        elif arrange_as == 'five-columns':
            result = [(MAX_WIDTH_1023PX, viewport_width)]

        return result

    def create_cell_state(self, value, context):

        result = SimpleNamespace()

        result.aspect_ratio = self.compute_aspect_ratio(value, context)
        result.content_fit = self.compute_content_fit(value, context)
        result.content_alignment = self.compute_content_alignment(value, context)
        result.padding = self.compute_padding(value, context)
        result.caption_alignment = self.compute_caption_alignment(value, context)
        result.default_size = self.compute_default_cell_size(value, context)
        result.conditional_sizes = self.compute_conditional_cell_sizes(value, context)
        result.image_filter_expr = value.get('image_filter_expr', '')

        return result

    def create_cell_for_item(self, item, render_index, source_index, annotations, cell_state):

        annotations['caption_label_css_class'] = \
            (annotations.get('caption_label_css_class', '') + ' ' + self.meta.caption_label_css_class).strip()
        annotations['figure_css_class'] = \
            (annotations.get('figure_css_class', '') + ' ' + self.meta.figure_css_class).strip()

        link = annotations.get('link', None)

        if link:
            link = ANNOTATION_LINK_BLOCK.to_python(link).as_rich_link()

        if link:
            link = link.determine_url()
            annotations['link'] = link

        if cell_state.caption_alignment:
            annotations['caption_alignment'] = cell_state.caption_alignment

        styles = {}

        if cell_state.padding:
            styles['padding'] = str(cell_state.padding)

        style_classes = []

        if cell_state.content_fit is not ResponsiveCell.FitContain:
            style_classes.append("figure-content")

        cell = ResponsiveCell(
            render_index=render_index,
            source_order=source_index,
            default_size=cell_state.default_size,
            conditional_sizes=cell_state.conditional_sizes,
            aspect_ratio=cell_state.aspect_ratio,
            content_fit=cell_state.content_fit,
            content_alignment=cell_state.content_alignment,
            styles=styles,
            style_classes=style_classes,
            annotations=annotations,
            image_filter_expr=cell_state.image_filter_expr,
            cells_by_media_condition=None)

        return cell

    def compute_root_element_css_classes(self, value, context):

        arrange_as = value.get('arrange_as', None)
        fit_width = value.get('fit_width', None)
        format_specifier = value.get('format', None)

        result = ' ' + self.root_element_css_classes.get(arrange_as, '')

        if fit_width == 'container':

            if format_specifier == 'viewport':
                result += ' fit-viewport'
            else:
                result += ''  # ' with-margins'

        elif fit_width == 'viewport':

            if format_specifier == 'viewport':
                result += ' fit-viewport borderless'
            else:
                result += ' borderless'

        result += ' ' + context.get('classname', '').strip()

        if self.meta.classname:
            result += ' ' + self.meta.classname.strip()

        if result:
            result = result[1:]

        return result

    def get_context(self, value, parent_context=None):

        context = super().get_context(value, parent_context)

        figure_id = 0

        anchor_category = value.get('anchor_category', '')

        if anchor_category:
            anchor_registry, inventory = current_anchor_registry_and_inventory()

            if anchor_registry:
                figure_id = anchor_registry.count_category(inventory, anchor_category)

        context.update({
            'css_classes': self.compute_root_element_css_classes(value, context),
            'figure': value,
            'figure_id': figure_id
        })

        return context


class SlideshowBlock(FigureBlock):

    slide_transition_choices = [
        ('fade', 'Fade'),
        ('scroll', 'Scroll')
    ]

    slide_transition_css_classes = {
        'fade': 'slide-transition-fade',
        'scroll': 'slide-transition-scroll'
    }

    class Meta:
        template = APP_LABEL + "/blocks/slideshow_block.html"
        figure_template = APP_LABEL + "/blocks/figure_block.html"
        slideshow_js_initiator = APP_LABEL + ".Slideshow"
        overlay_caption_css_class = "caption-overlay-style"

    slide_transition = blocks.ChoiceBlock(identifier='slide_transition', label='Slide Transition',
                                          choices=slide_transition_choices, default=slide_transition_choices[0][0])

    slide_pause = blocks.IntegerBlock(label='Slide Pause', default=10000)
    slide_auto_play_delay = blocks.IntegerBlock(label='Slide Auto-Play Delay', default=10000)
    overlay_captions = blocks.BooleanBlock(label='Overlay Captions', default_value=True, required=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        del self.child_blocks['arrange_as']

    def compute_default_cell_size(self, value, context):

        scale_factor = self.compute_scale_factor(value, context)
        result = CSSUnitValue(100.0 * scale_factor, CSSUnits.VIEW_WIDTH_UNIT)
        return result

    def compute_conditional_cell_sizes(self, value, context):

        MAX_WIDTH_409PX = "max-width: 409px"
        MAX_WIDTH_639PX = "max-width: 639px"
        MAX_WIDTH_1023PX = "max-width: 1023px"
        MAX_WIDTH_1599PX = "max-width: 1599px"

        scale_factor = self.compute_scale_factor(value, context)

        viewport_width = CSSUnitValue(100.0 * scale_factor, CSSUnits.VIEW_WIDTH_UNIT)
        result = [(MAX_WIDTH_409PX, viewport_width)]

        return result

    def create_cell_state(self, value, context):

        result = super().create_cell_state(value, context)

        overlay_captions = value.get('overlay_captions', False)
        result.overlay_caption = overlay_captions

        return result

    def create_cell_for_item(self, item, render_index, source_index, annotations, cell_state):

        if source_index == 0:
            annotations['figure_css_class'] = \
                (annotations.get('figure_css_class', '') + ' current-slide').strip()

        if cell_state.overlay_caption:
            annotations['caption_css_class'] = \
                (annotations.get('caption_css_class', '') + ' ' + self.meta.overlay_caption_css_class).strip()

        result = super().create_cell_for_item(item, render_index, source_index, annotations, cell_state)
        return result

    def compute_root_element_css_classes(self, value, context):
        result = super().compute_root_element_css_classes(value, context)
        result = ("slideshow " + result).strip()

        slide_transition = value.get('slide_transition', '')
        slide_transition = self.slide_transition_css_classes.get(slide_transition, '')

        if slide_transition:
            result += ' ' + slide_transition

        overlay_captions = value.get('overlay_captions', False)

        if overlay_captions:
            result += ' overlay-captions'

        return result

    # noinspection PyMethodMayBeStatic
    def compute_wrapper_element_css_classes(self, value, context):

        block_hints = self.get_block_hints(context)
        overlay_caption_placement = block_hints[OVERLAY_CAPTION_PLACEMENT_HINT].value()

        fit_width = value.get('fit_width', None)
        format_specifier = value.get('format', None)

        wrapper_css_classes = ' slideshow-container'

        if fit_width == 'container':

            if format_specifier == 'viewport':
                wrapper_css_classes += ' slideshow-viewport-container'
            else:
                wrapper_css_classes += ''  # ' slideshow-with-margins'

        elif fit_width == 'viewport':

            if format_specifier == 'viewport':
                wrapper_css_classes += ' slideshow-viewport-container borderless'
            else:
                wrapper_css_classes += ' borderless'

        overlay_captions = value.get('overlay_captions', False)

        if overlay_captions and overlay_caption_placement is not None:
            wrapper_css_classes += ' slide-caption-placement-' + overlay_caption_placement['value']

        if wrapper_css_classes:
            wrapper_css_classes = wrapper_css_classes[1:]

        return wrapper_css_classes

    def get_context(self, value, parent_context=None):

        context = super().get_context(value, parent_context)

        wrapper_css_classes = self.compute_wrapper_element_css_classes(value, context)

        context.update({
            'slideshow': value,
            'wrapper_css_classes': wrapper_css_classes,
            'wrapper_initiator': self.meta.slideshow_js_initiator
        })

        return context
