from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


def img_dir_path(instance, filename):
    return f"{instance.__class__.__name__}/{filename}"


class AbstractModel(models.Model):
    """Abstract base model for for all models."""

    class Meta:
        abstract = True

    image = models.ImageField(
        upload_to=img_dir_path,
        null=True,
        default="default.jpg",
    )
    title = models.CharField(
        "Title",
        help_text="Required",
        max_length=255,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
