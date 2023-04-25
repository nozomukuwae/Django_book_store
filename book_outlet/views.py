from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg, Min

from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all().order_by('-rating')
    books_count = books.count()
    aggregation = books.aggregate(Avg('rating'), Min('rating'))

    return render(request, 'book_outlet/index.html', {
        "books": books,
        "books_count": books_count,
        "aggregation": aggregation
    })

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(id=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        "book": book
    })