from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


class Author(models.Model):
    ''' Author atributes database '''
    name = models.TextField(max_length=50)
    age = models.IntegerField()
    city = models.TextField(max_length=50, null= True)
    country = models.TextField(max_length=50, null= True)
    state = models.TextField(max_length=50, null= True)
    user = models.ForeignKey(User,default=1)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('booksList:author_detail',
                       kwargs={'pk': self.pk})


class Books(models.Model):
    ''' Books atributes database '''
    title = models.TextField(max_length=50)
    author = models.ForeignKey(Author,default=1)
    isbn = models.IntegerField()
    date = models.DateTimeField(default=date.today())
    editorial = models.TextField(max_length=50)
    rating = models.IntegerField()
    reviews = models.IntegerField()
    genere = models.TextField(max_length=50)
    numPages = models.IntegerField()
    user = models.ForeignKey(User,default=1)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('booksList:books_detail',
                       kwargs={'pk': self.pk})

class Genere(models.Model):
    ''' Genere atributes '''
    name = models.TextField(max_length=50)

    def __unicode__(self):
        return self.name

class Review(models.Model):
    ''' Review atributes '''
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class BooksReview(Review):
    ''' Books ForeignKey '''
    books = models.ForeignKey(Books)

class AuthorReview(Review):
    ''' Author ForeignKey '''
    author = models.ForeignKey(Author)
