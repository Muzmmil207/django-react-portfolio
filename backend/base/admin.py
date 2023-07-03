from django.contrib import admin

from .models import (
    Author,
    BlogPosts,
    Contact,
    DeviceTrack,
    MyProject,
    NewsletterSubscriber,
    Tag,
)

admin.site.register(MyProject)
admin.site.register(Author)
admin.site.register(DeviceTrack)
admin.site.register(Contact)
admin.site.register(NewsletterSubscriber)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
    ]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(BlogPosts)
class BlogPostsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "draft",
        "created_at",
        "updated_at",
    ]
    list_filter = ["draft", "title"]
    prepopulated_fields = {"slug": ("title",)}
