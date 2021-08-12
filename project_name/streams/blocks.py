"""StreamFields"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtailmedia.blocks import AbstractMediaChooserBlock


class HeadingBlock(blocks.StructBlock):

    heading_text = blocks.CharBlock(
        required=True,
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

    quote_text = blocks.BlockQuoteBlock(label='Текст цитаты')

    quote_author = blocks.CharBlock(
        required=True,
        max_length=200,
        label='Автор цитаты',
    )

    class Meta:
        template = 'streams/quote_block.html'
        icon = 'openquote'
        label = 'Цитата'


class ImageBlock(blocks.StructBlock):

    image = ImageChooserBlock(label='Файл изображения')

    caption = blocks.CharBlock(
        required=True,
        max_length=250,
        label='Подпись',
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
            ('full_width', 'Справа'),
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
                    label='Подпись изображения', required=True, max_length=250,)),
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
        template = 'streams/table_block.html'
        icon = 'table'
        label = 'Таблица'


class ButtonsBlock(blocks.StructBlock):

    buttons_text = blocks.ListBlock(
        child_block=blocks.CharBlock(
            label='Кнопка',
            required=True,
            max_length=250,
        ),
        label='Кнопки'
    )

    button_direction = blocks.ChoiceBlock(
        choices=[
            ('horizontal', 'Горизонтальное'),
            ('vertical', 'Вертикальное'),
        ],
        label='Положение кнопок'
    )

    class Meta:
        template = 'streams/buttons_block.html'
        icon = 'tick-inverse'
        label = 'Кнопки'


class MediaAndTextBlock(blocks.StructBlock):

    text = blocks.RichTextBlock(label='Текст')

    media_content = blocks.StreamBlock(
        [
            ('image', ImageChooserBlock(label='Изображение')),
            ('video', EmbedBlock(label='Видео')),
        ],
        label='Медиа',
        max_num=1
    )

    position = blocks.ChoiceBlock(
        choices=[
            ('text_left', 'Текст слева'),
            ('text_right', 'Текст справа'),
        ],
        label='Положение текст'
    )

    class Meta:
        template = 'streams/media_and_text_block.html'
        icon = 'placeholder'
        label = 'Медиа и текст'


class FileBlock(DocumentChooserBlock):

    class Meta:
        template = 'streams/file_block.html'
        icon = 'doc-empty'
        label = 'Файл'


class AudioBlock(AbstractMediaChooserBlock):
    def render_basic(self, value, context=None):
        if not value:
            return ''

        if value.type == 'video':
            player_code = '''
            <div>
                <video width="320" height="240" controls>
                    {0}
                    Your browser does not support the video tag.
                </video>
            </div>
            '''
        else:
            player_code = '''
            <div>
                <audio controls>
                    {0}
                    Your browser does not support the audio element.
                </audio>
            </div>
            '''

        return format_html(player_code, format_html_join(
            '\n', "<source{0}>",
            [[flatatt(s)] for s in value.sources]
        ))

    class Meta:
        template = 'streams/audio_block.html'
        icon = 'media'
        label = 'Аудио'
