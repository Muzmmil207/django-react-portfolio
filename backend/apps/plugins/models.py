from django.db import models
from django.utils.translation import gettext_lazy as _


class MetaText(models.Model):
    class Meta:
        """Meta for MetaText."""
        verbose_name = _("Meta Text")
        verbose_name_plural = _("Meta Texts")

    key = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=255,
        verbose_name=_('Key'),
        help_text=_("It will be using to make a queryset"),
    )
    name = models.CharField(
        max_length=100,
        default="",
        verbose_name=_('Name'),
    )
    active = models.BooleanField(
        default=True,
        verbose_name=_('Active'),
        help_text=_("If False, it will return empty Response"),
    )

    def __str__(self) -> str:
        """Nice name."""
        name = f'{self.key}'
        if not self.active:
            name += '(not active)'
        return name


class TextContent(models.Model):
    """This model represents settings for individual Text Contents."""

    plugin = models.ForeignKey(
        MetaText,
        related_name='text_contents',
        null=False,
        verbose_name=_('Plugin'),
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        verbose_name=_('Content'),
    )
 
    def __str__(self) -> str:
        """Nice name."""
        name = f'{self.plugin.key}: {self.content[:30]}'
        if not self.plugin.active:
            name += '(not active)'
        return name

