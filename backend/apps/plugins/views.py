from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics

from .models import MetaText
from .serializers import MetaTextSerializer


class TextContentListView(
    generics.ListAPIView,
):

    serializer_class = MetaTextSerializer
    search_fields = ["key",]
        
    def get(self, request, format=None):
        return self.list(request)

    def get_queryset(self):
        queryset = MetaText.objects.filter(active=True).prefetch_related('text_contents')
        search_query = self.request.query_params.get("key")

        if search_query is not None:
            try:
                queryset = queryset.filter(
                    key__iexact=search_query
                )
            except ObjectDoesNotExist:
                queryset = None
    
        return queryset
