from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from audio_ebook.models import Book, Catalog, Subscribe
from audio_ebook.forms import BookForm, CatalogForm, SubscribeForm

class ValidationTest(TestCase):
    def test_book_valid(self):
        data = {'ISBN':'1000000000',
        'title':'Test Book',
        'author':'Test Test',
        'poster':'poster',
        'type_of_book':'Ebooks',
        'description':'description',
        'source':'source'}
        form = BookForm(data= data)
        self.assertTrue(form.is_valid())
    
    def test_catalog_valid(self):
        data = {'catalog_title':'Test Catalog',
        'genre':'Test Genre',
        'language':'Test Language',
        'booklist':''
        }
        form = CatalogForm(data= data)
        self.assertFalse(form.is_valid())

    def test_subscribe_valid(self):
        user = User.objects.create(username='test', password='1234test', email='test@test.com')
        catalog = Catalog.objects.create(catalog_title="Test Catalog", genre="Test Genre", language="Test Language")
        data = {'username':user, 'catalog':catalog}
        form = SubscribeForm(data= data)
        self.assertTrue(form.is_valid())

class LoginTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='test', password='1234test', email='test@test.com')

    def test_login(self):
        self.client.login(username='test', password='1234test')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response)

class BookPageTest(TestCase):
    
    def setUp(self):
        self.book = Book.objects.create(ISBN= '1000000000',
        title= 'Test Book',
        author= 'Test Test',
        poster= 'poster',
        type_of_book= 'Ebooks',
        description= 'description',
        source= 'source')
        
        self.response = self.client.get(reverse('book', args=(self.book.ISBN,)), follow=True)
    
    def test_book_page_url_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_book_template(self):
        self.assertTemplateUsed(self.response, "bookinfo.html")


class BookFieldTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(ISBN= '1000000000',
        title= 'Test Book',
        author= 'Test Test',
        poster= 'poster',
        type_of_book= 'Ebooks',
        description= 'description',
        source= 'source')

    def test_field_ISBN(self):
        field_label = self.book._meta.get_field('ISBN').verbose_name
        self.assertEqual(field_label, "ISBN")

    def test_field_title(self):
        field_label = self.book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, "title")
    
    def test_field_author(self):
        field_label = self.book._meta.get_field('author').verbose_name
        self.assertEqual(field_label, "author")

    def test_field_typeOfBook(self):
        field_label = self.book._meta.get_field('type_of_book').verbose_name
        self.assertEqual(field_label, "type of book")
    
    def test_field_description(self):
        field_label = self.book._meta.get_field('description').verbose_name
        self.assertEqual(field_label, "description")
    
    def test_field_source(self):
        field_label = self.book._meta.get_field('source').verbose_name
        self.assertEqual(field_label, "source")

class CatalogFieldTest(TestCase):
    def setUp(self):
        self.catalog = Catalog.objects.create(catalog_title="Test Catalog", genre="Test Genre", language="Test Language")

    def test_field_catalog_title(self):
        field_label = self.catalog._meta.get_field('catalog_title').verbose_name
        self.assertEqual(field_label, "catalog title")

    def test_field_title(self):
        field_label = self.catalog._meta.get_field('genre').verbose_name
        self.assertEqual(field_label, "genre")
    
    def test_field_author(self):
        field_label = self.catalog._meta.get_field('language').verbose_name
        self.assertEqual(field_label, "language")

    def test_field_typeOfBook(self):
        field_label = self.catalog._meta.get_field('booklist').verbose_name
        self.assertEqual(field_label, "booklist")

class SubscribeFieldTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='test', password='1234test', email='test@test.com')
        catalog = Catalog.objects.create(catalog_title="Test Catalog", genre="Test Genre", language="Test Language")
        self.subscribe = Subscribe.objects.create(username= user, catalog= catalog)

    def test_field_username(self):
        field_label = self.subscribe._meta.get_field('username').verbose_name
        self.assertEqual(field_label, "username")

    def test_field_title(self):
        field_label = self.subscribe._meta.get_field('catalog').verbose_name
        self.assertEqual(field_label, "catalog")