from django.contrib import admin
from .models import Book, Catalog, Subscribe

admin.site.register(Book)
admin.site.register(Catalog)
admin.site.register(Subscribe)