from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import PubliSerializer
from publication.models import Publication


class PubliViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all().order_by('-title')
    serializer_class = PubliSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticated]
