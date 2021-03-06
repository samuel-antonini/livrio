from rest_framework import serializers

from publication.models import Publication


class PubliSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        exclude = ['url']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        depth = 1
