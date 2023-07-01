from operator import mod

from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from utils.models.models_fields import AbstractModel

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField("Avatar", upload_to="authors/")
    occupation = models.TextField("Occupation", default="", max_length=500)
    company = models.CharField("Company", default="", max_length=75)
    twitter = models.URLField("Twitter", blank=True, null=True)
    linkedin = models.URLField("Linkedin", blank=True, null=True)
    github = models.URLField("Github", blank=True, null=True)
    last_activity = models.DateTimeField(
        "Last activity",
        default=timezone.now,
    )

    def __str__(self):
        return str(self.user)


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

    author = models.ManyToManyField(Author)
    summary = models.TextField(max_length=500)
    content = RichTextField(
        "Content",
    )
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField("Slug")
    draft = models.BooleanField(
        default=False,
        help_text="Draft post will not display",
    )
