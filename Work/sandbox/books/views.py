from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.views.generic import ListView
from books.models import Publisher
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from books.models import Book, Publisher

class PublisherBookList(ListView):

    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher,  name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)
class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'


def search_form(request):
    return render(request, 'books/search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})
