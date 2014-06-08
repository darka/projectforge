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

def reflections(request):
  reflections = Reflection.objects.filter()
  context = {'reflections': reflections}
  return render(request, 'treehouse/reflect.html', context)

def actions(request):
  actions = Action.objects.filter()
  context = {'actions': actions}
  return render(request, 'treehouse/actions.html', context)

def community(request):
  posts = Post.objects.filter()
  context = {'posts': posts}
  return render(request, 'treehouse/community.html', context)

