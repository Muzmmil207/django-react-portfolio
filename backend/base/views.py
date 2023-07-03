import json

from django.db.models import Count
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import mixins
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Author, BlogPosts, Contact, MyProject, NewsletterSubscriber, Tag
from .serializers import (
    ContactSerializer,
    MyProjectsSerializer,
    PostSerializer,
    TagsSerializer,
)


class CreateOnly(BasePermission):
    def has_permission(self, request, view):
        """Allow the unauthenticated users to send POST request only

        Returns:
            boolean: True | False
        """

        return request.method in ["POST"]


@api_view(["GET"])
def router(request, format=None):

    # from django_seed import Seed

    # seeder = Seed.seeder()
    # seeder.add_entity(Tag, 20)
    # seeder.add_entity(BlogPosts, 10)
    # seeder.add_entity(MyProject, 100)
    # seeder.add_entity(NewsletterSubscriber, 10)

    # inserted_pks = seeder.execute()
    return Response(
        {
            "Projects": reverse("projects-api", request=request, format=format),
            "Contacts": reverse("contact-api", request=request, format=format),
            "Posts": reverse("posts-api", request=request, format=format),
            "Post": reverse("post-api", args="a", request=request, format=format),
            "Tags": reverse("tags-api", request=request, format=format),
            "Subscribe": reverse("subscribe-api", request=request, format=format),
        }
    )


class TagsAPIView(generics.ListAPIView, mixins.ListModelMixin):
    serializer_class = TagsSerializer

    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset


@api_view(["GET"])
def posts_tags_api(request):
    data = dict()
    queryset = Tag.objects.all().annotate(Count("post_tags"))
    data.update({tag.get("name"): tag.get("post_tags__count") for tag in queryset.values()})

    return Response(data=data, status=status.HTTP_200_OK)


class PostsAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = BlogPosts.objects.all()
        tag = self.request.query_params.get("tag")

        if tag is not None:
            queryset = queryset.filter(tags__slug=tag)
        return queryset


class PostDetailsAPIView(generics.RetrieveAPIView, mixins.RetrieveModelMixin):
    serializer_class = PostSerializer
    lookup_field = "slug"
    queryset = BlogPosts.objects.all()


class ProjectsAPIView(generics.ListAPIView):
    serializer_class = MyProjectsSerializer
    queryset = MyProject.objects.all()


class ContactsAPIView(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = [IsAuthenticated | CreateOnly]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"data": "Thanks for reaching out! we'll be in touch soon."},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            data={"data": "Please provide valid data."},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["POST"])
def subscribe_handler(request):
    data = json.loads(request.body)
    try:
        subscribe = NewsletterSubscriber(
            email=data["email"],
        )
        subscribe.save()
        return Response(data={"done": True}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"done": False}, status=status.HTTP_400_BAD_REQUEST)
