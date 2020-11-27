from django.contrib import admin

from publicacoes.models import Publication


class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'isbn_ean', 'edition', 'year')


admin.site.register(Publication, PublicacaoAdmin)
