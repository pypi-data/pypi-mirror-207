import json

from django.template.loader import render_to_string

from wagtail.core import blocks as blocks

from django_auxiliaries.variable_scope import load_variable_scope

from wagtail_richer_text.blocks import RichTextBlock
from wagtail_switch_block.blocks import SwitchValue, DynamicSwitchBlock
from wagtail_switch_block.block_registry import BlockRegistry


from media_catalogue.settings import unify_media
from media_catalogue.models.universal_media_items import UniversalMediaItem

from .apps import get_app_label

__all__ = ['PointOfInterestValue', 'PointOfInterestBlock']

APP_LABEL = get_app_label()


class PointOfInterestValue(blocks.StructValue):

    def as_json(self):

        value = {
            "longitude": float(self["longitude"]),
            "latitude": float(self["latitude"]),
            "description": self["description"].__html__(),
            "showDescription": self["show_description"]
        }

        result = json.dumps(value)
        return result


class PointOfInterestBlock(blocks.StructBlock):

    class Meta:
        icon = 'link'
        value_class = PointOfInterestValue
        default = {}

    longitude = blocks.DecimalBlock(label="Longitude", default=-0.126100, required=False)
    latitude = blocks.DecimalBlock(label="Latitude", default=51.522823, required=False)
    description = RichTextBlock(label="Formatted Text", editor=APP_LABEL + '.pointofinterestdescription', required=False)
    show_description = blocks.BooleanBlock(label="Show Description", required=False, default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        _, args, kwargs = super(PointOfInterestBlock, self).deconstruct()

        if args:
            args = args[1:]

        path = APP_LABEL + '.blocks.PointOfInterestBlock'
        return path, args, kwargs


class MapViewerBlockRegistry(BlockRegistry):

    # noinspection PyMethodMayBeStatic
    def should_register_block(self, app_label, local_identifier, block_type, block_args, block_kwargs, **kwargs):
        if not issubclass(block_type, MapViewerMixin):
            raise RuntimeError("Registered block type must be a subclass of MapViewerMixin")

        return True

    # noinspection PyMethodMayBeStatic
    def should_include_entry_for_container_block(self, identifier, entry, container_block):
        return True

    # noinspection PyMethodMayBeStatic
    def instantiate_block(self, identifier, entry, container_block):
        block_kwargs = dict(entry.block_kwargs)

        block = entry.block_type(*entry.block_args, **block_kwargs)
        block.set_name(identifier)

        return block


MAP_VIEWER_BLOCK_REGISTRY = MapViewerBlockRegistry()
MAP_VIEWER_BLOCK_REGISTRY.define_procedures_in_caller_module("map_viewer")


class MapViewerMixin:

    def map_view_to_universal_media_item(self, map_view):

        if unify_media():
            universal_media_item = UniversalMediaItem.objects.get(content_id=map_view.pk,
                                                                  content_type=map_view.content_type.id)
        else:
            universal_media_item = map_view

        return universal_media_item

    def prepare_context(self, configuration, map_view, cell, context):

        universal_media_item = self.map_view_to_universal_media_item(map_view)

        scope = load_variable_scope(APP_LABEL, map_view_index=0)
        scope.map_view_index += 1

        context.update({
            'media_item': map_view,
            'universal_media_item': universal_media_item,
            'handle': 'map-view-' + '{:d}'.format(scope.map_view_index)
        })

        context['container_style'] = ''
        context['container_class'] = ''

        if cell.use_aspect_ratio:
            context['container_style'] = "--aspect-ratio: {};".format(cell.aspect_ratio_as_text)

        if cell.styles:
            context['container_style'] += " " + cell.formatted_styles

        if cell.style_classes:
            context['container_class'] = cell.formatted_style_classes

    def render_in_responsive_cell(self, configuration, map_view, cell, context=None):
        return None


MapViewerValue = SwitchValue


class MapViewerBlock(MapViewerMixin, DynamicSwitchBlock):

    class Meta:
        map_viewer_blocks_function_name = APP_LABEL + ".blocks.map_viewer_block_choices"
        choice_label = "Select Map Viewer"

    def __init__(self, *args, **kwargs):

        map_viewer_blocks_function_name = kwargs.pop("map_viewer_blocks_function_name",
                                                    self._meta_class.map_viewer_blocks_function_name) # noqa

        super().__init__(*args,
                         map_viewer_blocks_function_name=map_viewer_blocks_function_name,
                         child_blocks_function_name=map_viewer_blocks_function_name,
                         **kwargs)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs

    def render_in_responsive_cell(self, configuration, map_view, cell, context=None):

        map_viewer_block = self.child_blocks[configuration.type]
        return map_viewer_block.render_in_responsive_cell(configuration.value, map_view, cell, context)


class LeafletViewerBlock(MapViewerMixin, blocks.StructBlock):

    class Meta:
        view_template = APP_LABEL + '/blocks/leaflet_viewer_block.html'

    interaction = blocks.StructBlock([
        ('enable_scroll_wheel_zoom', blocks.BooleanBlock(label='Enable Scroll Wheel Zoom', default=False, required=False)),
        ('enable_touch_zoom', blocks.BooleanBlock(label='Enable Touch Zoom', default=True, required=False)),
        ('enable_dragging', blocks.BooleanBlock(label='Enable Dragging', default=True, required=False)),
        ('enable_touch_dragging', blocks.BooleanBlock(label='Enable Touch Dragging', default=True, required=False))
        ])

    options = blocks.StructBlock([
        ('show_attribution', blocks.BooleanBlock(label='Show Attribution', default=False, required=False)),
        ('show_zoom_control', blocks.BooleanBlock(label='Show Zoom Control', default=True, required=False))
        ])

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        return context

    def render_in_responsive_cell(self, configuration, map_view, cell, context=None):
        context = self.get_context(configuration, parent_context=context)
        self.prepare_context(configuration, map_view, cell, context)
        result = render_to_string(self.meta.view_template, context=context)
        return result


register_map_viewer_block(APP_LABEL, "leaflet_viewer", LeafletViewerBlock, [], {}) # noqa
