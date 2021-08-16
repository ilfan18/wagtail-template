# Generated by Django 3.2.5 on 2021-08-13 11:12

from django.db import migrations
import project_name.streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail_color_panel.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('inner_pages', '0014_alter_textpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpage',
            name='content',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(label='Текст заголовка', max_length=250)), ('heading_size', wagtail.core.blocks.ChoiceBlock(choices=[('H2', 'H2'), ('H3', 'H3'), ('H4', 'H4')], label='Размер заголовка'))])), ('richtext', project_name.streams.blocks.RichTextBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote_text', wagtail.core.blocks.RichTextBlock(label='Текст цитаты')), ('quote_author', wagtail.core.blocks.CharBlock(label='Автор цитаты', max_length=200, required=False)), ('quote_reference', wagtail.core.blocks.CharBlock(label='Источник цитаты', required=False))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Файл изображения')), ('image_caption', wagtail.core.blocks.CharBlock(label='Подпись', max_length=250, required=False)), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Слева'), ('center', 'В центре'), ('right', 'Справа'), ('full-width', 'По ширине')], label='Положение изображения'))])), ('embed', wagtail.core.blocks.StructBlock([('embed_url', wagtail.embeds.blocks.EmbedBlock(label='Ссылка на ресурс')), ('embed_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Слева'), ('center', 'В центре'), ('right', 'Справа'), ('full_width', 'По ширине')], label='Положение контента'))])), ('slider', wagtail.core.blocks.StructBlock([('images', wagtail.core.blocks.ListBlock(child_block=wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('caption', wagtail.core.blocks.CharBlock(label='Подпись изображения', max_length=250, required=True))]), label='Изображения в слайдере'))])),
                                                  ('gallery', wagtail.core.blocks.StructBlock([('images', wagtail.core.blocks.ListBlock(child_block=wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('caption', wagtail.core.blocks.CharBlock(label='Подпись изображения', max_length=250, required=True))]), label='Изображения в галлерее'))])), ('table', project_name.streams.blocks.TableBlock()), ('buttons', wagtail.core.blocks.StructBlock([('buttons_text', wagtail.core.blocks.ListBlock(child_block=wagtail.core.blocks.CharBlock(label='Кнопка', max_length=250, required=True), label='Кнопки')), ('buttons_direction', wagtail.core.blocks.ChoiceBlock(choices=[('horizontal', 'Горизонтальное'), ('vertical', 'Вертикальное')], label='Положение кнопок')), ('buttons_color', wagtail_color_panel.blocks.NativeColorBlock(default='#000000'))])), ('media_and_text', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(label='Текст')), ('media_content', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('video', wagtail.core.blocks.StructBlock([('embed_url', wagtail.embeds.blocks.EmbedBlock(label='Ссылка на ресурс')), ('embed_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Слева'), ('center', 'В центре'), ('right', 'Справа'), ('full_width', 'По ширине')], label='Положение контента'))], label='Видео'))], label='Медиа', max_num=1)), ('position', wagtail.core.blocks.ChoiceBlock(choices=[('text_left', 'Текст слева'), ('text_right', 'Текст справа')], label='Положение текст'))])), ('file', project_name.streams.blocks.FileBlock()), ('audio', project_name.streams.blocks.MediaBlock())], blank=True, null=True),
        ),
    ]
