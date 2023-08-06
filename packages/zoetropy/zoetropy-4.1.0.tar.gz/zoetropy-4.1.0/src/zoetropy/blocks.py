
from wagtail_content_block.annotations import *
from media_catalogue.blocks import MediaItemChooserBlock, MediaItemChooserBlockValue

__all__ = ['PosterChooserBlock', 'PosterChooserBlockValue', 'POSTER_ANNOTATIONS']


POSTER_ANNOTATIONS = ContentAnnotations(groups=[

            ContentAnnotationGroup(
                identifier='credits',
                label='Credits',
                fields=[
                    TextAnnotationField(
                        identifier='category',
                        label='',
                        default_value='Image',
                        attributes={
                            'placeholder': ''
                        }
                    ),

                    TextAreaAnnotationField(
                        identifier='names',
                        label='Name(s)',
                        attributes={
                            'placeholder': ''
                        }
                    )
                ]
            )
        ])


PosterChooserBlockValue = MediaItemChooserBlockValue


class PosterChooserBlock(MediaItemChooserBlock):

    class Meta:
        annotations = POSTER_ANNOTATIONS
