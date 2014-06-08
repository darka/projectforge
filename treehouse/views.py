from django.shortcuts import render
from django.views import generic
from treehouse.models import *

from datetime import date

def books(request):
  books = Book.objects.filter()
  context = {'books': books}
  return render(request, 'treehouse/list_books.html', context)

def book(request, object_id):
  book = Book.objects.get(pk=object_id)
  context = {'book': book}
  return render(request, 'treehouse/book.html', context)

def reflection(request):
  pass

def action(request):
  pass

def post(request):
  pass
