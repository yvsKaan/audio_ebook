from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields

from .models import Book, Catalog, Subscribe

class BookForm(forms.ModelForm):
    class Meta:
        model= Book
        fields= ("ISBN", "title", "author", "poster", "type_of_book", "description")

class CatalogForm(forms.ModelForm):
    class Meta:
        model= Catalog
        fields= ("catalog_title", "genre", "language", "booklist")


class SubscribeForm(forms.ModelForm):
    class Meta:
        model= Subscribe
        fields= ("username", "catalog")