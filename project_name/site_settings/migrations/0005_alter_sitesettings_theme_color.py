# Generated by Django 3.2.5 on 2021-08-02 10:37

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0004_alter_sitesettings_theme_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='theme_color',
            field=colorfield.fields.ColorField(default='#FFFFFFFF', help_text='Цвет интерфейса и вкладки браузера Android, фона плитки в Windows', max_length=18, verbose_name='Цветовая тема'),
        ),
    ]