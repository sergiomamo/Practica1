from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Author(models.Model):
    name = models.TextField(max_length=50)
    age = models.IntegerField()
    country = models.TextField(max_length=50)
    nacionalidad = models.TextField(max_length=50)
    user = models.ForeignKey(User,default=1)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('booksList:author_detail',
                       kwargs={'pk': self.pk})


class Books(models.Model):
    title = models.TextField(max_length=50)
    author = models.TextField(max_length=50)
    isbn = models.IntegerField()
    date = models.DateTimeField()
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
    name = models.TextField(max_length=50)

    def __unicode__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class BooksReview(Review):
    books = models.ForeignKey(Books)

class AuthorReview(Review):
    author = models.ForeignKey(Author)
