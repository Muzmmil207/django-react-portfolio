from ckeditor.fields import RichTextField
from django.db import models
from utils.models.models_fields import AbstractModel


class Tag(models.Model):
    class Meta:
        """Meta options for the model"""

        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        db_table = "tags"

    name = models.CharField(
        "Name",
        help_text="Required",
        max_length=25,
        unique=True,
    )


class BlogPosts(AbstractModel):
    class Meta:
        """Meta options for the model"""

        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        db_table = "blog_post"
        ordering = ("-updated_at", "-created_at")

    summary = models.TextField(max_length=500)
    content = RichTextField(
        "Content",
    )
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField("Slug")
    draft = models.BooleanField(default=False)
