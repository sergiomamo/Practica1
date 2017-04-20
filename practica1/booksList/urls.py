from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView

from models import Author, Books, Genere
from forms import BooksForm
from views import BooksCreate, BooksDetail, review, mainpage

urlpatterns = [
    # List latest 5 restaurants: /booksList/
    url(r'^$', TemplateView.as_view(template_name = 'base.html'), name='home'),
    url(r'^books/$',
        ListView.as_view(
            queryset=Books.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_books_list',
            template_name='books/books_list.html'),
        name='books_list'),

    # Restaurant details, ex.: /myrestaurants/restaurants/1/
    url(r'^books/(?P<pk>\d+)/$',
        BooksDetail.as_view(),
        name='books_detail'),

    # Create a restaurant, /myrestaurants/restaurants/create/
    url(r'^books/create/$',
        BooksCreate.as_view(),
        name='books_create'),

    # Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    url(r'^books/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Books,
            template_name='booksList/form.html',
            form_class=BooksForm),
        name='books_edit'),

    # Create a restaurant review, ex.: /myrestaurants/restaurants/1/reviews/create/
    url(r'^books/(?P<pk>\d+)/reviews/create/$',
        review,
        name='review_create'),
]
