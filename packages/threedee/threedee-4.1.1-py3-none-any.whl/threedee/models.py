import os

from media_catalogue.models import MediaItem
from .paraview_import import parse_paraview_webgl_content_html_text

from django.core.files.storage import default_storage as DEFAULT_STORAGE
from django.utils.functional import cached_property
from django.db.models import DecimalField, CharField, BooleanField, FloatField
from django.template.loader import get_template, render_to_string
from django.template.context import make_context, Context
from django.template.loader_tags import IncludeNode
from django.template.defaultfilters import safe

from wagtail.admin.panels import FieldPanel, FieldRowPanel, MultiFieldPanel

from media_catalogue.settings import unify_media
from media_catalogue.models.universal_media_items import UniversalMediaItem

from .apps import get_app_label

APP_LABEL = get_app_label()


class ParaviewWebGLModel(MediaItem):

    @classmethod
    def get_attachment_range(cls):
        return 1, 1

    class Meta:
        verbose_name = 'Paraview Model'
        verbose_name_plural = 'Paraview Models'

    template_path = APP_LABEL + "/paraview_webgl_model.html"

    vector_layout_specifier = CharField(verbose_name="Vector Layout", max_length=20, default="0 1 2")
    flip_normals = BooleanField(verbose_name="Flip Normals", default=False)

    override_up_vector = BooleanField(verbose_name="Override", default=False)
    up_vector_definition = CharField(verbose_name="Definition", max_length=20, default="0 1 0")

    override_orientation = BooleanField(verbose_name="Override", default=False)
    rotation = DecimalField(verbose_name="Rotation (Deg)", blank=True, default=0.0, decimal_places=2, max_digits=5)
    elevation = DecimalField(verbose_name="Elevation (Deg)", blank=True, default=30.0, decimal_places=2, max_digits=5)

    use_device_pixels = BooleanField(verbose_name="Use Device Pixels", default=False, help_text="Use native/higher resolution on HiDPI screens.")
    zoom_factor = FloatField(verbose_name="Zoom Factor", default=0.0, help_text="Initial zoom factor.")

    panels = MediaItem.panels + [
        # FieldPanel("vector_layout_specifier"),
        # FieldPanel("flip_normals"),
        FieldRowPanel([FieldPanel("override_up_vector"),
                       FieldPanel("up_vector_definition")], heading="Camera Up Vector"),
        MultiFieldPanel(
            [FieldPanel("override_orientation"),
             FieldRowPanel([FieldPanel("rotation"), FieldPanel("elevation")])],
            heading="Camera Orientation"
        ),
        MultiFieldPanel(
            [FieldPanel("use_device_pixels"), FieldPanel("zoom_factor")],
            heading="Presentation"
        )
    ]

    @cached_property
    def stream_size(self):
        path = os.path.join(self.content_path, 'object_streams.bin')

        try:
            return DEFAULT_STORAGE.size(path)
        except BaseException:
            return 0

    @property
    def vector_layout(self):
        result = [0, 1, 2]
        parts = self.vector_layout_specifier.strip().split()  # noqa

        if len(parts) != 3:
            return result

        try:
            parts = [int(p) for p in parts]
        except ValueError:
            return result

        if 0 not in parts or 1 not in parts or 2 not in parts:
            return result

        return parts

    @property
    def up_vector(self):
        result = [0, 1, 0]
        parts = self.up_vector_definition.strip().split()  # noqa

        if len(parts) != 3:
            return result

        try:
            parts = [float(p) for p in parts]
        except ValueError:
            return result

        return parts

    @staticmethod
    def will_be_deleted(instance, **kwargs):
        MediaItem.will_be_deleted(instance, **kwargs)
        pass

    @staticmethod
    def was_deleted(instance, **kwargs):
        MediaItem.was_deleted(instance, **kwargs)
        pass

    @cached_property
    def metadata_json(self):

        storage = DEFAULT_STORAGE

        metadata_file = storage.open(self.content_path + "metadata.json")
        metadata = metadata_file.read().decode('utf-8')
        return metadata

    def render_in_responsive_cell(self, cell, template_context=None):

        # template = get_template(self.template_path)
        # return template.render(context_data)

        if unify_media():
            universal_media_item = UniversalMediaItem.objects.get(content_id=self.pk, content_type=self.content_type.id)
        else:
            universal_media_item = self

        if template_context is None:
            template_context = make_context({})

        template_context.update({
            'media_item': self,
            'universal_media_item': universal_media_item
        })

        if cell.use_aspect_ratio:
            template_context['container_style'] = "--aspect-ratio: {};".format(cell.aspect_ratio_as_text)

        if cell.styles:
            template_context['container_style'] += " " + cell.formatted_styles

        # template = get_template(self.get_template_path(), using=None)
        template_path = safe(self.get_template_path())

        class TemplateWrapper:

            def __init__(self, template_path):
                self.template_path = template_path

            def resolve(self, context, ignore_failures=False):
                template = get_template(self.template_path, using=None)
                return template

        include = IncludeNode(
            TemplateWrapper(template_path))

        result = include.render(template_context)
        return result

    def assemble(self):

        attachment = self.attachments_for_role_identifier('paraview_html').first()

        _ = self.stream_size
        del self.stream_size  # noqa Remove cached stream_size
        self.delete_contents()

        if attachment is None:
            return

        paraview_html = attachment.read_text()
        paraview_content = parse_paraview_webgl_content_html_text(paraview_html)

        self.generate_preview_image()
        paraview_content.save(DEFAULT_STORAGE, self.content_path)
