import os


from django.core.files.storage import default_storage as DEFAULT_STORAGE
from django.core.files.base import ContentFile
from django.utils.functional import cached_property
from django.db.models import CharField, ForeignKey, PositiveIntegerField
import django.db.models as django_models
from django.utils.translation import ngettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils.html import escape

from urllib.parse import quote as urlquote

from wagtail.admin.panels import FieldPanel
from wagtail.admin.forms.models import register_form_field_override
from wagtail.images.rect import Rect

from markup_adaptation.svg_template import SVGContent, SVGTemplate

from media_catalogue.models import MediaItem

from aldine.render import render_content_in_responsive_cell

from csskit.common import CSSUnits

from .apps import get_app_label

__all__ = ['VectorGraphic']

APP_LABEL = get_app_label()


class VectorGraphic(MediaItem):

    @classmethod
    def get_attachment_range(cls):
        return 0, 1

    @cached_property
    def svg_text(self):

        storage = DEFAULT_STORAGE

        try:
            content_file = storage.open(self.content_path + "regular.svg")
        except FileNotFoundError:

            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'vector_graphics',
                                'svg', 'broken_link.svg')
            content_file = open(path, "rb")

        content_svg_text = content_file.read().decode('utf-8')

        return content_svg_text

    @cached_property
    def svg_content(self):

        storage = DEFAULT_STORAGE

        try:
            content_file = storage.open(self.content_path + "regular.svg")
        except FileNotFoundError:

            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'vector_graphics',
                                'svg', 'broken_link.svg')
            content_file = open(path, "rb")

        svg_content = SVGContent.from_binary_file(content_file)

        return svg_content

    @cached_property
    def svg_content_orientation(self):
        svg_content = SVGContent.from_text(self.svg_text)
        view_box = svg_content.view_box

        if view_box[2] > view_box[3]:
            return "landscape"

        if view_box[2] == view_box[3]:
            return "square"

        return "portrait"

    @cached_property
    def svg_content_url(self):
        return self.content_path + "regular.svg"

    @cached_property
    def svg_template(self):
        result = SVGTemplate.from_text(self.svg_text)
        return result

    @property
    def preview_image_path(self):
        return self.svg_content_url

    @property
    def preview_image_url(self):
        return DEFAULT_STORAGE.url(self.preview_image_path)

    @property
    def has_preview_image(self):
        return True

    def generate_preview_image(self):
        pass

    def render_preview_html(self):

        if self.svg_content_orientation != "portrait":
            return mark_safe('<img src="{}" width="165" />'.format(self.preview_image_url))
        else:
            return mark_safe(
                '<img src="{}" height="165" max-height="165" style="height: 165px;"/>'.format(self.preview_image_url))

    @cached_property
    def inline_image(self):

        tmp = self.svg_text
        tmp = urlquote(tmp)
        tmp = escape(tmp)
        tmp = "<img src='data:image/svg+xml;charset=utf-8," + tmp + "'>"

        return tmp

    #@cached_property
    #def configuration_schema(self):
    #    template = self.svg_template
    #    return template.schema

    class Meta:
        verbose_name = 'Vector Graphic'
        verbose_name_plural = 'Vector Graphics'

    template_path = "vector_graphics/vector_graphic.html"

    focal_point_x = PositiveIntegerField(null=True, blank=True)
    focal_point_y = PositiveIntegerField(null=True, blank=True)
    focal_point_width = PositiveIntegerField(null=True, blank=True)
    focal_point_height = PositiveIntegerField(null=True, blank=True)

    derived_from = ForeignKey(APP_LABEL + ".VectorGraphic", related_name="derivations",
                              on_delete=django_models.SET_NULL,
                              default=None, null=True, blank=True)

    panels = MediaItem.panels + [
    ]

    def get_focal_point(self):
        if (
            self.focal_point_x is not None
            and self.focal_point_y is not None
            and self.focal_point_width is not None
            and self.focal_point_height is not None
        ):
            return Rect.from_point(
                self.focal_point_x,
                self.focal_point_y,
                self.focal_point_width,
                self.focal_point_height,
            )

    def has_focal_point(self):
        return self.get_focal_point() is not None

    def set_focal_point(self, rect):
        if rect is not None:
            self.focal_point_x = rect.centroid_x
            self.focal_point_y = rect.centroid_y
            self.focal_point_width = rect.width
            self.focal_point_height = rect.height
        else:
            self.focal_point_x = None
            self.focal_point_y = None
            self.focal_point_width = None
            self.focal_point_height = None

    @staticmethod
    def render_content(cell, svg_content, dimensions, adjustments, alignment, attributes, layout_sizes):

        # Remove any pre-defined height, width and aspect ratio
        svg_content.width = None
        svg_content.height = None
        svg_content.preserve_aspect_ratio = None
        svg_content.pointer_events = "none"

        # Get the view box (to retrieve the intrinsic aspect ratio)
        view_box = svg_content.view_box

        # Render the content in the selected rendition sizes

        svg_content.view_box = \
            view_box[0] - adjustments[3], view_box[1] - adjustments[0], dimensions[0], dimensions[1]

        svg_pos = translate_content_position_to_svg((alignment[0] * 100, alignment[1] * 100),
                                                    (CSSUnits.PERCENTAGE_UNIT, CSSUnits.PERCENTAGE_UNIT))

        if cell.content_fit is cell.FitFill:
            preserve_aspect_ratio = None
        elif cell.content_fit is cell.FitCover:
            preserve_aspect_ratio = svg_pos, 'slice'
        else:
            preserve_aspect_ratio = svg_pos, 'meet'

        svg_content.preserve_aspect_ratio = preserve_aspect_ratio
        svg_content.svg_attributes.update(attributes)

        text = svg_content.to_text()
        return mark_safe(text)

    def render_in_responsive_cell(self, cell, template_context=None):

        svg_content = SVGContent.from_text(self.svg_text)

        # Remove any pre-defined height, width and aspect ratio
        svg_content.width = None
        svg_content.height = None
        svg_content.preserve_aspect_ratio = None
        svg_content.pointer_events = "none"

        # Get the view box (to retrieve the intrinsic aspect ratio)
        view_box = svg_content.view_box
        intrinsic_dimensions = view_box[2], view_box[3]

        focal_point = self.get_focal_point()

        return render_content_in_responsive_cell(svg_content, intrinsic_dimensions, focal_point, cell, self.render_content)

    def assemble(self):

        attachment = self.attachments_for_role_identifier('svg').first()

        if attachment is not None:

            vector_graphic = SVGContent.from_binary_file(attachment.file)
            self.delete_contents()
            save_svg_content(vector_graphic, DEFAULT_STORAGE, self.content_path)

        elif self.derived_from is not None:
            pass


def translate_content_percentage_to_svg(pos):
    if pos <= 25.0:
        return 'Min'

    if pos <= 75.0:
        return 'Mid'

    return 'Max'


def translate_content_position_to_svg(pos, units):
    pos_h, pos_v = pos
    pos_h_units, pos_v_units = units

    if pos_h_units != CSSUnits.PERCENTAGE_UNIT:
        svg_pos_h = 'xMid'
    else:
        svg_pos_h = 'x' + translate_content_percentage_to_svg(pos_h)

    if pos_v_units != CSSUnits.PERCENTAGE_UNIT:
        svg_pos_v = 'YMid'
    else:
        svg_pos_v = 'Y' + translate_content_percentage_to_svg(pos_v)

    return svg_pos_h + svg_pos_v


def save_svg_content(svg_content, storage, path):
    svg_text = svg_content.to_text()

    svg_file = ContentFile(svg_text)
    storage.save(path + "regular.svg", svg_file)


"""
register_form_field_override(
    ForeignKey, to=VectorGraphic,
    override={"widget": AdminContentChooser(
                'media_catalogue:chooser',
                max_num_choices=1,
                content_type_filter=([ContentType.objects.get_for_model(VectorGraphic).pk], True))
    }
)
"""
