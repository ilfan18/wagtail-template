from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


@register_setting
class SiteSettings(BaseSetting, ClusterableModel):
    """Global site settings model."""

    company_name = models.CharField(
        verbose_name='Название вашей компании',
        max_length=200,
        blank=True,
        null=True
    )

    description = models.CharField(
        verbose_name='Описание',
        max_length=250,
        blank=True,
        null=True,
        help_text='Вид деятельности вашей компании'
    )

    tagline = models.CharField(
        verbose_name='Слоган вашей компании',
        max_length=200,
        blank=True,
        null=True
    )

    logo = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Логотип',
        help_text='Рекомендуемые размеры изображения 100x100'
    )

    favicon = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Иконка',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Рекомендуемые размеры изображения 260x260'
    )

    site_copyright = models.CharField(
        verbose_name='Копирайт вашей компании',
        max_length=200,
        blank=True,
        null=True
    )

    panels = [
        FieldPanel('company_name'),
        FieldPanel('description'),
        FieldPanel('tagline'),
        ImageChooserPanel('logo'),
        MultiFieldPanel(
            [
                InlinePanel('header_phones', label='Телефоны'),
                InlinePanel('header_adresses', label='Адреса'),
                InlinePanel('header_socials', label='Социальные сети'),
                InlinePanel('header_emails', label='Адреса электронной почты'),
            ],
            heading='Контакты в шапке'
        ),
        MultiFieldPanel(
            [
                InlinePanel('footer_phones', label='Телефоны'),
                InlinePanel('footer_adresses', label='Адреса'),
                InlinePanel('footer_socials', label='Социальные сети'),
                InlinePanel('footer_emails', label='Адреса электронной почты'),
            ],
            heading='Контакты в подвале'
        ),
        FieldPanel('site_copyright'),
        ImageChooserPanel('favicon', heading='Фавикон'),
    ]

    class Meta:
        verbose_name = 'Глобальные настройки'


class PhoneItemHeader(Orderable):
    parent = ParentalKey(
        'SiteSettings',
        on_delete=models.CASCADE,
        related_name='header_phones'
    )

    phone_num = models.CharField(
        verbose_name='Телефон',
        max_length=20,
        blank=True,
        null=True
    )

    panels = [
        FieldPanel('phone_num'),
    ]


class AdressItemHeader(Orderable):
    parent = ParentalKey(
        'SiteSettings',
        on_delete=models.CASCADE,
        related_name='header_adresses'
    )

    adress_text = models.CharField(
        verbose_name='Адрес',
        max_length=200,
        blank=True,
        null=True
    )

    panels = [
        FieldPanel('adress_text'),
    ]


class SocialItemHeader(Orderable):
    parent = ParentalKey(
        'SiteSettings',
        on_delete=models.CASCADE,
        related_name='header_socials'
    )

    title = models.CharField(
        verbose_name='Название',
        max_length=200,
        blank=True,
        null=True
    )

    link = models.CharField(
        verbose_name='Ссылка',
        max_length=200,
        blank=True,
        null=True
    )

    icon = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Иконка',
        help_text='Рекомендуемые размеры изображения 30x30'
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('link'),
        ImageChooserPanel('icon'),
    ]


class EmailItemHeader(Orderable):
    parent = ParentalKey(
        'SiteSettings',
        on_delete=models.CASCADE,
        related_name='header_emails'
    )

    email_text = models.CharField(
        verbose_name='Э-мейл',
        max_length=20,
        blank=True,
        null=True
    )

    panels = [
        FieldPanel('email_text'),
    ]


class PhoneItemFooter(Orderable):
    parent = ParentalKey(
        'SiteSettings',
        on_delete=models.CASCADE,
        related_name='footer_phones'
    )

    phone_num = models.CharField(
        verbose_name='Телефон',
        max_length=20,
        blank=True,
        null=True
    )

    panels = [
        FieldPanel('phone_num'),
    ]


class AdressItemFooter(Orderable):
    parent = ParentalKey(
        'SiteSettings',
        on_delete=models.CASCADE,
        related_name='footer_adresses'
    )

    adress_text = models.CharField(
        verbose_name='Адрес',
        max_length=200,
        blank=True,
        null=True
    )

    panels = [
        FieldPanel('adress_text'),
    ]


class SocialItemFooter(Orderable):
    parent = ParentalKey(
        'SiteSettings',
        on_delete=models.CASCADE,
        related_name='footer_socials'
    )

    title = models.CharField(
        verbose_name='Название',
        max_length=200,
        blank=True,
        null=True
    )

    link = models.CharField(
        verbose_name='Ссылка',
        max_length=200,
        blank=True,
        null=True
    )

    icon = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Иконка',
        help_text='Рекомендуемые размеры изображения 30x30'
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('link'),
        ImageChooserPanel('icon'),
    ]


class EmailItemFooter(Orderable):
    parent = ParentalKey(
        'SiteSettings',
        on_delete=models.CASCADE,
        related_name='footer_emails'
    )

    email_text = models.CharField(
        verbose_name='Э-мейл',
        max_length=20,
        blank=True,
        null=True
    )

    panels = [
        FieldPanel('email_text'),
    ]
