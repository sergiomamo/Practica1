from django.conf.urls import url, patterns, include
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns	import format_suffix_patterns

from models import Author, Books, Genere
from forms import BooksForm, AuthorForm
from views import BooksCreate, AuthorCreate, BooksDetail, AuthorDetail, reviewBooks, mainpage, \
    AuthorDelete, BooksDelete,reviewAuthor, AuthorListAPI, AuthorDetailAPI, BooksListAPI, BooksDetailAPI,\
    APIBooksReviewList, APIBooksReviewDetail

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
            template_name='form.html',
            form_class=BooksForm),
        name='books_edit'),

    url(r'^author/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Author,
            template_name='form.html',
            form_class=AuthorForm),
        name='author_edit'),

    url(r'^books/(?P<pk>\d+)/reviews/create/$',
        reviewBooks,
        name='review_books_create'),

    url(r'^author/(?P<pk>\d+)/reviews/create/$',
        reviewAuthor,
        name='review_author_create'),

    url(r'^author/(?P<pk>\d+)/delete/$',
        AuthorDelete,
        name='author_delete'),

    url(r'^books/(?P<pk>\d+)/delete/$',
        BooksDelete,
        name='books_delete'),

    # RESTful API
    url(r'^api/author/$', AuthorListAPI.as_view(), name='author-list'),
    url(r'^api/author/(?P<pk>\d+)/$', AuthorDetailAPI.as_view(), name='author-detail'),
    url(r'^api/books/$', BooksListAPI.as_view(), name='books-list'),
    url(r'^api/books/(?P<pk>\d+)/$', BooksDetailAPI.as_view(), name='books-detail'),

    url(r'^api/booksreviews/$',
        APIBooksReviewList.as_view(), name='booksreview-list'),
    url(r'^api/booksreviews/(?P<pk>\d+)/$',
        APIBooksReviewDetail.as_view(), name='booksreview-detail'),
]

#	Format	suffixes
urlpatterns	= format_suffix_patterns(urlpatterns, allowed=['json', 'api'])


#	Default	login/logout	views
urlpatterns	+= patterns('',
                url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
