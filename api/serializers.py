from rest_framework import serializers
from scrapy.spidermiddlewares import depth

from publicacoes.models import Publication


class PubliSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        exclude = ['url']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        depth = 1
