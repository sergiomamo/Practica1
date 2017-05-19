from django.contrib.auth.models	import User, Group, Permission
from rest_framework import serializers
from models import Author, Books, Genere


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'age', 'country', 'nacionalidad')


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'isbn', 'editorial', 'rating', 'reviews', 'genere', 'numPages')