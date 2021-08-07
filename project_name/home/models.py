from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    """Home page model."""

    max_count = 1
    is_main = True

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Титульная страница'
