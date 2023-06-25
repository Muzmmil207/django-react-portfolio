from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


class AbstractModel(models.Model):
    """Abstract base model for for all models."""
    class Meta:
        abstract = True

    title = models.CharField(
        "Title",
        help_text="Required",
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        unique=False,
        blank=False,
        verbose_name="Safe URL",
        help_text="format: required, letters, numbers, underscore, or hyphens",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

