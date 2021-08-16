"""StreamFields"""
from django.utils.html import format_html, format_html_join
from django.forms.utils import flatatt
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtailmedia.blocks import AbstractMediaChooserBlock
from wagtail_color_panel.blocks import NativeColorBlock


class HeadingBlock(blocks.StructBlock):

    heading_text = blocks.CharBlock(
        max_length=250,
        label='Текст заголовка',
    )

    heading_size = blocks.ChoiceBlock(
        choices=[
            ('H2', 'H2'),
            ('H3', 'H3'),
            ('H4', 'H4'),
        ],
        label='Размер заголовка',
    )

    class Meta:
        template = 'streams/heading_block.html'
        icon = 'title'
        label = 'Заголовок'


class RichTextBlock(blocks.RichTextBlock):

    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'edit'
        label = 'Текст'


class QuoteBlock(blocks.StructBlock):

    quote_text = blocks.RichTextBlock(
        label='Текст цитаты',
    )

    quote_author = blocks.CharBlock(
        required=False,
        max_length=200,
        label='Автор цитаты',
    )

    quote_reference = blocks.CharBlock(
        required=False,
        label='Источник цитаты',
    )

    class Meta:
        template = 'streams/quote_block.html'
        icon = 'openquote'
        label = 'Цитата'


class ImageBlock(blocks.StructBlock):

    image = ImageChooserBlock(label='Файл изображения')

    image_caption = blocks.CharBlock(
        required=False,
        max_length=250,
        label='Подпись',
    )

    image_position = blocks.ChoiceBlock(
        choices=[
            ('left', 'Слева'),
            ('center', 'В центре'),
            ('right', 'Справа'),
            ('full-width', 'По ширине'),
        ],
        label='Положение изображения'
    )

    class Meta:
        template = 'streams/image_block.html'
        icon = 'image'
        label = 'Изображение'


class EmbedBlock(blocks.StructBlock):

    embed = EmbedBlock(label='Ссылка на ресурс')

    embed_position = blocks.ChoiceBlock(
        choices=[
            ('left', 'Слева'),
            ('center', 'В центре'),
            ('right', 'Справа'),
            ('full-width', 'По ширине'),
        ],
        label='Положение контента'
    )

    class Meta:
        template = 'streams/embed_block.html'
        icon = 'media'
        label = 'Встраиваемый контент'


class SliderBlock(blocks.StructBlock):

    images = blocks.ListBlock(
        child_block=blocks.StructBlock(
            [
                ('image', ImageChooserBlock(label='Изображение')),
                ('caption', blocks.CharBlock(
                    label='Подпись изображения', required=False, max_length=250,)),
            ]
        ),
        label='Изображения в слайдере'
    )

    class Meta:
        template = 'streams/slider_block.html'
        icon = 'placeholder'
        label = 'Слайдер'


class GalleryBlock(blocks.StructBlock):

    images = blocks.ListBlock(
        child_block=blocks.StructBlock(
            [
                ('image', ImageChooserBlock(label='Изображение')),
                ('caption', blocks.CharBlock(
                    label='Подпись изображения', required=True, max_length=250,)),
            ]
        ),
        label='Изображения в галлерее'
    )

    class Meta:
        template = 'streams/gallery_block.html'
        icon = 'placeholder'
        label = 'Галлерея'


class TableBlock(TableBlock):

    class Meta:
        icon = 'table'
        label = 'Таблица'


class ButtonsBlock(blocks.StructBlock):

    buttons_items = blocks.ListBlock(
        child_block=blocks.StructBlock(
            [
                ('text', blocks.CharBlock(
                    label='Текст кнопки',
                    max_length=250,
                )),
                ('url', blocks.PageChooserBlock(label='Ссылка')),
            ],
            label='Кнопка'
        ),
        label='Кнопки'
    )

    buttons_direction = blocks.ChoiceBlock(
        choices=[
            ('horizontal', 'Горизонтальное'),
            ('vertical', 'Вертикальное'),
        ],
        label='Положение кнопок'
    )

    buttons_color = NativeColorBlock(default="#000000", label='Цвет кнопок')

    class Meta:
        template = 'streams/buttons_block.html'
        icon = 'tick-inverse'
        label = 'Кнопки'


class ImageAndTextBlock(blocks.StructBlock):

    text = blocks.RichTextBlock(label='Текст')

    image = ImageChooserBlock(label='Изображение')

    position = blocks.ChoiceBlock(
        choices=[
            ('text_left', 'Текст слева'),
            ('text_right', 'Текст справа'),
        ],
        label='Положение текста'
    )

    class Meta:
        template = 'streams/image_and_text_block.html'
        icon = 'placeholder'
        label = 'Изображение и текст'


class FileBlock(DocumentChooserBlock):

    class Meta:
        template = 'streams/file_block.html'
        icon = 'doc-empty'
        label = 'Файл'


class MediaBlock(AbstractMediaChooserBlock):

    def __str__(self):
        return self.title

    class Meta:
        template = 'streams/media_block.html'
        icon = 'media'
        label = 'Медиа'
