from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import mixins
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import Author, BlogPosts, Contact, MyProject, Tag
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

    return Response(
        {
            "Projects": reverse("projects-api", request=request, format=format),
            "Contacts": reverse("contact-api", request=request, format=format),
            "Posts": reverse("posts-api", request=request, format=format),
            "Tags": reverse("tags-api", request=request, format=format),
        }
    )


class TagsAPIView(generics.ListAPIView):
    serializer_class = TagsSerializer
    queryset = Tag.objects.all()


class PostsAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = BlogPosts.objects.all()


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
