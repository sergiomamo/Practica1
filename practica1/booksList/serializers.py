from django.contrib.auth.models	import User, Group, Permission
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework import serializers

from models import Author, Books, BooksReview


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'age', 'country', 'nacionalidad')


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'isbn', 'editorial', 'rating', 'reviews', 'genere', 'numPages')


class BooksReviewSerializer(serializers.HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='booksList:booksreview-detail')
    books = HyperlinkedRelatedField(view_name='booksList:books-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = BooksReview
        fields = ('uri', 'rating', 'comment', 'user', 'date', 'books')