from ckeditor.fields import RichTextField
from django.db import models
from imagekit.models import ProcessedImageField


class MyProject(models.Model):
    class Meta:
        db_table = "my_projects"

    title = models.CharField(
        "Title",
        help_text="Required",
        max_length=255,
        unique=True,
    )
    image = ProcessedImageField(
        upload_to="images",
        format="PNG",
        options={"quality": 100},
    )
    description = RichTextField(
        "Description",
        help_text="Not Required",
        blank=True,
    )
    src_url = models.URLField(
        "Source Code Url",
        help_text="Required",
    )
    project_url = models.URLField(
        "project_url",
        help_text="Not Required",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField("Is Active", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
