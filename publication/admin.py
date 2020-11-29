from django.contrib import admin

from publication.models import Publication


class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'isbn_ean', 'edition', 'year')
    list_filter = ('category',)
    search_fields = ('author',)


admin.site.register(Publication, PublicacaoAdmin)
