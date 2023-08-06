import json
import os
import re

from media_catalogue.models import MediaItem

from django.core.files.storage import default_storage

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.db.models import DecimalField, IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator

from wagtail.admin.panels import FieldPanel, FieldRowPanel
from wagtail.models import StreamField

from wagtail_block_model_field.fields import BlockModelField

from .blocks import PointOfInterestBlock, MapViewerBlock, MapViewerValue
from .apps import get_app_label

__all__ = ['MapView']

APP_LABEL = get_app_label()


def validate_identifier(value):
    if re.search(r"(^[^A-Za-z0-9_]|\s)", value):
        raise ValidationError(
            _("Identifiers must start with a letter, a digit or underscore "
              "and cannot contain whitespace characters: {:}").format(value)
        )


def get_schema_upload_path(self, filename):
    # if not default_storage.exists(filename):
    filename = default_storage.get_valid_name(filename)

    # noinspection PyUnresolvedReferences
    filename = filename.encode('ascii', errors='replace').decode('ascii')

    # noinspection PyUnresolvedReferences
    path = os.path.join(self.path, filename)

    if len(path) >= 95:
        chars_to_trim = len(path) - 94
        prefix, extension = os.path.splitext(filename)
        filename = prefix[:-chars_to_trim] + extension
        # noinspection PyUnresolvedReferences
        path = os.path.join(self.path, filename)

    return path


def to_camel_case(string):
    first, *others = string.split('_')
    return ''.join([first.lower(), *map(str.title, others)])


class MapView(MediaItem):

    @classmethod
    def get_attachment_range(cls):
        return None, None

    class Meta:
        verbose_name = 'Map View'
        verbose_name_plural = 'Map Views'

    longitude = DecimalField(verbose_name="Longitude", default=-0.09, decimal_places=12, max_digits=15)
    latitude = DecimalField(verbose_name="Latitude", default=51.505, decimal_places=12, max_digits=15)
    zoom_level = IntegerField(verbose_name="Zoom Level", default=13,
                              validators=[MinValueValidator(1), MaxValueValidator(18)])

    annotations = StreamField([("point_of_interest", PointOfInterestBlock(label="Point of Interest"))],
                              use_json_field=True, blank=True, null=True, default={})

    viewer = BlockModelField(MapViewerBlock(), value_class=MapViewerValue)

    panels = MediaItem.panels + [

        FieldRowPanel([FieldPanel("longitude"), FieldPanel("latitude")], heading="Location"),
        FieldPanel("zoom_level"),

        FieldPanel("viewer"),

        FieldPanel("annotations")
    ]

    @staticmethod
    def will_be_deleted(instance, **kwargs):
        MediaItem.will_be_deleted(instance, **kwargs)
        pass

    @staticmethod
    def was_deleted(instance, **kwargs):
        MediaItem.was_deleted(instance, **kwargs)
        pass

    @property
    def metadata(self):

        result = {
            'viewer': 'default',
            'longitude': float(self.longitude),  # noqa
            'latitude': float(self.latitude),  # noqa
            'zoomLevel': self.zoom_level,
            'configuration': self.viewer.value # noqa
        }

        return result

    @property
    def metadata_json(self):

        result = json.dumps(self.metadata)
        return result

    def render_in_responsive_cell(self, cell, template_context=None):

        viewer_block = self.__class__.viewer.field.block_def # noqa
        return viewer_block.render_in_responsive_cell(
                    self.viewer, self, cell, context=template_context.flatten() if template_context else None)

    def assemble(self):
        return
