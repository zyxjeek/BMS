from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Book
from .forms import BookForm


# Create your views here.
def index(request):
    return render(request, 'system/index.html')


def book(request, id):
    bk = Book.objects.get(id=id)
    context = {'book': bk}
    return render(request, 'system/book.html', context)


def books(request):
    bks = Book.objects.order_by('date_added')
    context = {'books': bks}
    return render(request, 'system/books.html', context)


def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books')
    else:
        form = BookForm()
    return render(request, 'system/new_book.html', context={'form': form})
