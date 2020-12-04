from rest_framework import generics
from rest_framework import permissions

from api.serializers import PubliSerializer
from publication.models import Publication


class PublicationList(generics.ListAPIView):
    serializer_class = PubliSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Publication.objects.all().order_by('title')
        author = self.request.query_params.get('author', None)
        people = self.request.query_params.get('people', None)
        isbn = self.request.query_params.get('isbn', None)
        if author is not None:
            queryset = Publication.objects.filter(author__icontains=author)
        elif people is not None:
            queryset = Publication.objects.filter(people__icontains=people)
        elif isbn is not None:
            queryset = Publication.objects.filter(isbn_ean=isbn)

        return queryset
