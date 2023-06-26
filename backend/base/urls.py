from django.contrib.flatpages.views import flatpage
from django.urls import re_path as url

from . import views

urlpatterns = [
    url(r"^$", views.router),
    url(r"^projects$", views.ProjectsAPIView.as_view(), name="projects-api"),
    url(r"^contacts$", views.ContactsAPIView.as_view(), name="contact-api"),
    url(r"^posts$", views.PostAPIView.as_view(), name="posts-api"),
]
