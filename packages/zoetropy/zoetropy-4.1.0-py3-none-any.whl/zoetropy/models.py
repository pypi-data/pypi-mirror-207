import os

from media_catalogue.models import MediaItem

from django.core.files.storage import default_storage as DEFAULT_STORAGE
from django.core.files.base import ContentFile
from django.db import models as django_models
from django.template.loader import get_template
from django.template.context import make_context
from django.template.loader_tags import IncludeNode
from django.template.defaultfilters import safe

from wagtail.admin.panels import FieldPanel, FieldRowPanel

from wagtail_block_model_field.fields import BlockModelField

from media_catalogue.settings import unify_media
from media_catalogue.models.universal_media_items import UniversalMediaItem


from .apps import get_app_label
from .blocks import *

APP_LABEL = get_app_label()


class VideoClip(MediaItem):

    @classmethod
    def get_attachment_range(cls):
        return 1, 1

    class Meta:
        verbose_name = "Video Clip"
        verbose_name_plural = "Video Clips"

    CROSS_ORIGIN_CHOICES = [("none", "None"), ("anonymous", "Anonymous"), ("use-credentials", "Use Credentials")]
    PRELOAD_CHOICES = [("none", "None"), ("auto", "Auto"), ("metadata", "Metadata")]

    template_path = APP_LABEL + "/video_clip.html"

    cross_origin = django_models.CharField(max_length=64, choices=CROSS_ORIGIN_CHOICES, default=CROSS_ORIGIN_CHOICES[0][0])
    show_controls = django_models.BooleanField(default=False, blank=True, null=True)

    autoplay = django_models.BooleanField(default=True, blank=True, null=True)
    loop = django_models.BooleanField(default=False, blank=True, null=True)
    muted = django_models.BooleanField(default=True, blank=True, null=True)
    preload = django_models.CharField(max_length=64, choices=PRELOAD_CHOICES, default=PRELOAD_CHOICES[2][0])

    poster = BlockModelField(PosterChooserBlock(equired=False), value_class=PosterChooserBlockValue,
                             blank=True, null=True)

    panels = MediaItem.panels + [
        FieldPanel("cross_origin"),
        FieldPanel("show_controls"),
        FieldRowPanel(
            [
                FieldPanel("autoplay"),
                FieldPanel("loop"),
                FieldPanel("muted"),
            ]
        ),

        FieldPanel("preload"),
        FieldPanel("poster")
    ]

    @staticmethod
    def will_be_deleted(instance, **kwargs):
        MediaItem.will_be_deleted(instance, **kwargs)

    @staticmethod
    def was_deleted(instance, **kwargs):
        MediaItem.was_deleted(instance, **kwargs)

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

        template_context['container_style'] = template_context.get('container_style', '') + \
            " " + "width: 100%; height: 100%; object-fit: cover; object-position: 50% 50%;"

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

        self.delete_contents()

        for attachment in self.attachments_for_role_identifier('video'):
            video_file = attachment.read_bytes()
            video_file = ContentFile(video_file)
            file_name = os.path.basename(attachment.file.name)
            DEFAULT_STORAGE.save(self.content_path + file_name, video_file)
