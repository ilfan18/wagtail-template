from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from project_name.streams import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import (
    ListBlock,
    CharBlock,
    StructBlock,
)


class TextPage(Page):
    """Text page model."""

    subtitle = models.CharField(
        verbose_name='Подзаголовок',
        max_length=200,
        blank=True,
        null=True
    )

    content = StreamField(
        [
            ('heading', blocks.HeadingBlock()),
            ('richtext', blocks.RichTextBlock()),
            ('quote', blocks.QuoteBlock()),
            ('image', blocks.ImageBlock()),
            ('embed', blocks.EmbedBlock()),
            ('slider', blocks.SliderBlock()),
            ('gallery', blocks.GalleryBlock()),
            ('table', blocks.TableBlock()),
            ('buttons', blocks.ButtonsBlock()),
            ('media_and_text', blocks.ImageAndTextBlock()),
            ('file', blocks.FileBlock()),
            ('audio', blocks.MediaBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', heading='Подзаголовок'),
        StreamFieldPanel('content', heading='Контент страницы')
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Текстовая страница'
