from django import forms
import datetime

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = None
        labels = {'title': '书名', 'price': '价格', 'author': '作者'}
