from django.urls import re_path as url

from . import views

urlpatterns = [
    url(r"^$", views.router),
    url(r"^projects$", views.ProjectsAPIView.as_view(), name="projects-api"),
    url(r"^contacts$", views.ContactsAPIView.as_view(), name="contact-api"),
    url(r"^posts$", views.PostsAPIView.as_view(), name="posts-api"),
    url(r"^posts/(?P<slug>[a-z0-9-.,*?]+)$", views.PostDetailsAPIView.as_view(), name="post-api"),
    url(r"^tags$", views.TagsAPIView.as_view(), name="tags-api"),
]
