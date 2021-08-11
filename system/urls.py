from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/<int:id>', views.book, name='book'),
    path('books', views.books, name='books'),
    path('new_book', views.new_book, name='new_book'),
]
