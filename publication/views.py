import json
import os

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from publication.models import Publication


@login_required
def loader(request):
    directory = settings.DATA_DUMP_FOLDER

    Publication.objects.all().delete()

    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)

        with open(file) as base_file:
            json_obj = json.load(base_file)
            base_file.close()

        for book in json_obj:
            data = {
                'title': str(book['title']).split('-')[0].strip(),
                'author': book['author'],
                'publisher': book['publisher'],
                'isbn_ean': book['isbn_ean'],
                'category': book['category'],
                'language': book['language'],
                'format': book['publi_format'],
                'pages': book['pages'],
                'edition': book['edition'],
                'year': book['year'],
                'people': book['people'],
                'cover_url': book['images'][0]['path'],
                'blurb': str(book['blurb']).replace("[", "").replace(']', '').replace("'", "").replace('"', '').strip(),
            }

            publi = Publication(**data)
            publi.save()

    return HttpResponse('arquivo importado com sucesso.')
