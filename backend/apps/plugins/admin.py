from django.contrib import admin

from .models import MetaText, TextContent


class TextContentInline(admin.TabularInline):
    model = TextContent


@admin.register(MetaText)
class MetaTextAdmin(admin.ModelAdmin):
    inlines = [
        TextContentInline,
    ]

admin.site.register(TextContent)
