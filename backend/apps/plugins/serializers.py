from rest_framework import serializers

from .models import MetaText, TextContent


class TextContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextContent
        fields = [
            "content",
        ]


class MetaTextSerializer(serializers.ModelSerializer):

    text_contents = TextContentSerializer(many=True)

    class Meta:
        model = MetaText
        fields = [
            "id",
            "key",
            "name",
            "text_contents",
        ]
    