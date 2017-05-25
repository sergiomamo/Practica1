from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, render_to_response
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from models import Author, Books, Genere, BooksReview, AuthorReview
from forms import BooksForm, AuthorForm

from rest_framework	import generics
from rest_framework.decorators	import api_view
from rest_framework.reverse	import reverse
from rest_framework.response	import Response
from serializers import AuthorSerializer, BooksSerializer, BooksReviewSerializer


def mainpage(request):
    ''' Return template base.html '''
    return render_to_response('base.html')


class BooksDetail(DetailView):
    ''' Return Books detail, use template books_detail.html '''
    model = Books
    template_name = 'books/books_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BooksDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = BooksReview.RATING_CHOICES
        return context


class AuthorDetail(DetailView):
    ''' Return Author detail, use template author_detail.html '''
    model = Author
    template_name = 'author/author_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = AuthorReview.RATING_CHOICES
        return context


class BooksCreate(CreateView):
    ''' Create Books, use template form.html '''
    model = Books
    template_name = 'form.html'
    form_class = BooksForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BooksCreate, self).form_valid(form)


class AuthorCreate(CreateView):
    ''' Create Author, use template form.html '''
    model = Author
    template_name = 'form.html'
    form_class = AuthorForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AuthorCreate, self).form_valid(form)


def reviewBooks(request, pk):
    books = get_object_or_404(Books, pk=pk)
    #if BooksReview.objects.filter(books=books, user=request.user).exists():
     #   BooksReview.objects.get(books=books, user=request.user).delete()
    reviews = BooksReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        books=books)
    reviews.save()
    return HttpResponseRedirect(reverse('booksList:books_detail', args=(books.id,)))


def reviewAuthor(request, pk):
    author = get_object_or_404(Author, pk=pk)
    reviews = AuthorReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        author=author)
    reviews.save()
    return HttpResponseRedirect(reverse('booksList:author_detail',
                                        args=(author.id,)))


def AuthorDelete(request, pk):
    '''Author delete'''
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return HttpResponseRedirect(reverse('booksList:author_list', ))


def BooksDelete(request, pk):
    '''Books delete'''
    books = get_object_or_404(Books, pk=pk)
    books.delete()
    return HttpResponseRedirect(reverse('booksList:books_list', ))



@api_view(['GET'])
def api_root(request, format=None):
    """
    The	entry endpoint of our API.
    """
    return Response({
        'author': reverse('author-list', request=request),
        'books': reverse('books-list', request=request),
    })


class AuthorListAPI(generics.ListCreateAPIView):
    """
    API	endpoint that represents a list	of	author.
    """
    model = Author
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    API	endpoint that represents a single author.
    """
    model = Author
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BooksListAPI(generics.ListCreateAPIView):
    """
    API	endpoint that represents a list of books.
    """
    model = Books
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    API	endpoint	that	represents	a	single	books.
    """
    model = Books
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class APIBooksReviewList(generics.ListCreateAPIView):
    model = BooksReview
    queryset = BooksReview.objects.all()
    serializer_class = BooksReviewSerializer


class APIBooksReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    model = BooksReview
    queryset = BooksReview.objects.all()
    serializer_class = BooksReviewSerializer