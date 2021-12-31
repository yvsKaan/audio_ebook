from django.contrib import admin
from django.urls import path,include

from audio_ebook.views import Home, RegisterFormView, BookView, CatalogList, BookList, Library

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('catalogs/', CatalogList.as_view(), name='catalogs'),
    path('books/', BookList.as_view(), name='books'),
    path('library/', Library.as_view(), name='library'),
    path('book/<pk>', BookView.as_view(), name='book'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterFormView.as_view(), name="register"),
    path('admin/', admin.site.urls),
]
