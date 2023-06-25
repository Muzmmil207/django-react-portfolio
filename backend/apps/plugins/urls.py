from django.urls import path

from . import views

urlpatterns = [
    path("text-content", views.TextContentListView.as_view()),
]
