from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, ListView, FormView, DetailView

from .models import Book, Catalog, Subscribe
from django.db.models import Q, query
from .forms import BookForm, CatalogForm, SubscribeForm

class Home(ListView):
    #a book via its title, author or ISBN catalog by genre, language or subject
    def get(self, request):
        if request.user.is_authenticated:
            catalog_queryset = Catalog.objects.filter(catalog_title = "Recommend")
            search = request.GET.get("search", "")
            if search:
                catalog_queryset = Catalog.objects.filter(
                    Q(catalog_title__icontains = search)|
                    Q(genre__icontains = search)|
                    Q(language__icontains = search)
                )
                book_queryset = Book.objects.filter(
                    Q(title__icontains = search)|
                    Q(ISBN = search)|
                    Q(author__icontains = search)
                )
                context = {
                'catalog_list': catalog_queryset,
                'book_list': book_queryset,
                'search': search
                }
            else: 
                context = {
                'recommend_catalog': catalog_queryset,
                }
            return render(request, "index.html", context)
        else: 
            return redirect('login')

class CatalogList(View):
    queryset = Catalog.objects.all()

    def get(self, request):
        context = {
            "catalog_list": self.queryset,
        }

        return render(request, "cataloglist.html", context)
    
    def post(self, request):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
        context = {
            "catalog_list": self.queryset
        }
        return render(request, "cataloglist.html", context)
    


class BookList(View):
    model = Book
    def get(self, request):
        queryset = self.model.objects.all()
        context = {
            "book_list": queryset.order_by('title'),
        }

        return render(request, "booklist.html", context)

class BookView(DetailView):
    model = Book
    template_name = "bookinfo.html"


class Library(View):
    model = Subscribe
    def get(self, request):
        queryset = self.model.objects.filter(username = request.user.id)
        context = {
            "library_list": queryset,
        }

        return render(request, "library.html", context)
    
class RegisterFormView(FormView):
    template_name = "registration/register.html"
    form_class = UserCreationForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
            return render(request, "registration/register.html", {'form': form})

class RegisterFormView(FormView):
    template_name = "registration/register.html"
    form_class = UserCreationForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
            return render(request, "registration/register.html", {'form': form})