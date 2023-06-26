from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import Contact, MyProject, Post, PostSource
from .serializers import ContactSerializer, MyProjectsSerializer, PostSourceSerializer


class CreateOnly(BasePermission):
    def has_permission(self, request, view):
        """Allow the unauthenticated users to send POST request only

        Returns:
            boolean: True | False
        """

        return request.method in ["POST"]


@api_view(["GET"])
def router(request, format=None):
    print(request.META)  # ["HTTP_USER_AGENT"])
    print(request.META)  # ["HTTP_REMOTE_ADDER"])
    return Response(
        {
            "Projects": reverse("projects-api", request=request, format=format),
            "Contacts": reverse("contact-api", request=request, format=format),
            "Posts": reverse("posts-api", request=request, format=format),
        }
    )


class PostAPIView(generics.ListAPIView):
    serializer_class = PostSourceSerializer
    queryset = PostSource.objects.all()


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
            return Response(data={"": ""}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.default_validators, status=status.HTTP_400_BAD_REQUEST)
