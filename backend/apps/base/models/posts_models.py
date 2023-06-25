from django.db import models
from utils.models.models_fields import AbstractModel


class PostSource(models.Model):
    class Meta:
        db_table = "posts_source"

    source_name = models.CharField(
        max_length=40,
        verbose_name="post source",
    )


class Post(AbstractModel):
    source = models.ManyToManyField(PostSource, related_name="source")
    post_url = models.URLField(
        "project_url",
        help_text="Required",
    )

    def __str__(self):
        return self.title
