from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Book(models.Model):
    Audiobook = 'Audiobook'
    EBook = 'Ebooks'
    BOOK_TYPE = [
        (Audiobook, 'Audiobook'),
        (EBook, 'Ebooks'),
    ]
    
    ISBN = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    poster = models.CharField(max_length=500)
    type_of_book = models.CharField(max_length=10, choices=BOOK_TYPE, default=EBook)
    description = models.CharField(max_length=800)
    source = models.CharField(max_length=800, default="")
    
    def __str__(self):
        return self.ISBN + "-" + self.title

class Catalog(models.Model):
    catalog_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    booklist = models.ManyToManyField(Book)

    def __str__(self):
        return self.catalog_title

class AudiobookDetail(models.Model):
    ISBN = models.OneToOneField(Book, on_delete=CASCADE)
    chapter_id = models.IntegerField()
    start_time = models.CharField(max_length=8)
    end_time = models.CharField(max_length=8)

class Subscribe(models.Model):
    username = models.ForeignKey(User, on_delete=CASCADE)
    catalog = models.ForeignKey(Catalog, on_delete=CASCADE)