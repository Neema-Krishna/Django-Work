from django.shortcuts import render
from django.http import Http404

from .models import Book
from django.db.models import Avg,Max,Min


# Create your views here.

def index(request):
    Books=Book.objects.all().order_by('title')
    books_count=Books.count()
    avg_rating=Books.aggregate(Avg("rating"))

    return render(request,'book_outlet/index.html',{'books':Books,'Number_of_books':books_count,'avg_rating':avg_rating})

def detail(request,slug):
    try:
     book=Book.objects.get(slug=slug)
    except:
       raise Http404()
    return render(request,'book_outlet/bookdetail.html',
                   {'title':book.title,
                    'author':book.author,
                    'rating':book.rating,
                    'is_bestseller':book.is_bestselling})

