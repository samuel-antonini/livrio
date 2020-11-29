from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Publication(models.Model):
    title = models.CharField(max_length=150)
    author = models.JSONField()
    publisher = models.CharField(max_length=25)
    isbn_ean = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=25, blank=True, null=True)
    format = models.CharField(max_length=25, blank=True, null=True)
    pages = models.CharField(max_length=4, blank=True, null=True)
    edition = models.CharField(max_length=2, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    people = models.JSONField(blank=True, null=True)
    slug = models.SlugField(max_length=200, default='', editable=False)
    cover_url = models.CharField(max_length=150, blank=True, null=True)
    blurb = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('publi-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = f"{self.title} {self.edition}ed"
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
