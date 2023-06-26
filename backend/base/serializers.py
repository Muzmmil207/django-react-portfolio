from rest_framework import serializers

from .models import Contact, MyProject, Post, PostSource


class MyProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProject
        fields = [
            "id",
            "title",
            "image",
            "description",
            "src_url",
            "project_url",
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "image",
            "title",
            "post_url",
        ]


class PostSourceSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True)

    class Meta:
        model = PostSource
        fields = "__all__"
