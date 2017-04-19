from django import forms
from models import Book

class BooksForm(ModelForm):
    class Meta:
        model = Book
