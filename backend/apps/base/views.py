from rest_framework import generics
from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Contact, MyProject, Post, PostSource
from .serializers import ContactSerializer, MyProjectsSerializer, PostSerializer


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
            "all Projects": reverse("projects-api", request=request, format=format),
            "contacts": reverse("contact-api", request=request, format=format),
        }
    )

class PostAPIView(APIView):
    ...
class ProjectsAPIView(generics.ListAPIView):
    serializer_class = MyProjectsSerializer
    queryset = MyProject.objects.all()


class ContactsAPIView(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = [IsAuthenticated | CreateOnly]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
