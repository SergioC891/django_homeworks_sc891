from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_objects = Book.objects.all().order_by('name')
    books = []

    for book in books_objects:
        book = {
            'name': book.name,
            'author': book.author,
            'pub_date': f'{book.pub_date}',
        }
        books.append(book)

    context = {
        'books': books,
    }
    return render(request, template, context)


def books_view_pub_date(request, pub_date):
    template = 'books/books_list.html'

    books_objects = Book.objects.filter(pub_date=pub_date).order_by('name')
    books_prev_date = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date')
    books_next_date = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date')
    books = []
    prev_date = ''
    next_date = ''

    if books_prev_date:
        prev_date = books_prev_date[0].pub_date
    if books_next_date:
        next_date = books_next_date[0].pub_date

    for book in books_objects:
        book = {
            'name': book.name,
            'author': book.author,
            'pub_date': f'{book.pub_date}',
        }
        books.append(book)

    context = {
        'books': books,
        'prev_date': prev_date,
        'next_date': next_date,
        'prev_date_formated': f'{prev_date}',
        'next_date_formated': f'{next_date}',
    }
    return render(request, template, context)
