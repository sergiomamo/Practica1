from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView

from models import Author, Books, Genere
from forms import BooksForm, AuthorForm
from views import BooksCreate, AuthorCreate, BooksDetail, AuthorDetail, review, mainpage, reviewAuthor

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name = 'base.html'), name='home'),
    url(r'^books/$',
        ListView.as_view(
            queryset=Books.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_books_list',
            template_name='books/books_list.html'),
        name='books_list'),

    url(r'^author/$',
        ListView.as_view(
            queryset=Author.objects.filter().order_by('user')[:5],
            context_object_name='latest_author_list',
            template_name='author/author_list.html'),
        name='author_list'),

    url(r'^books/(?P<pk>\d+)/$',
        BooksDetail.as_view(),
        name='books_detail'),

    url(r'^author/(?P<pk>\d+)/$',
        AuthorDetail.as_view(),
        name='author_detail'),

    url(r'^books/create/$',
        BooksCreate.as_view(),
        name='books_create'),

    url(r'^author/create/$',
        AuthorCreate.as_view(),
        name='author_create'),

    url(r'^books/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Books,
            template_name='booksList/form.html',
            form_class=BooksForm),
        name='books_edit'),

    url(r'^author/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Author,
            template_name='booksList/form.html',
            form_class=AuthorForm),
        name='books_edit'),

    url(r'^books/(?P<pk>\d+)/reviews/create/$',
        review,
        name='review_create'),

    url(r'^author/(?P<pk>\d+)/reviews/create/$',
        reviewAuthor,
        name='review_create'),
]
