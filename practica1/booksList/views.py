from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Context
from django.template.loader import get_template


# Create your views here.
def mainpage(request):
    return render_to_response('base.html',{
        'appname': "booksList",
        'titlepage': 'Books',
        "author": "Eduard i Sergio"
    })

"""class BookDetail(DetailView):
    model = Books
    template_name = 'templates/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = BookReview.RATING_CHOICES
        return context"""

def dashboard(request, usuari):
    #si no existe el usuario devuelve una excepcion
    try:
        user = User.objects.get(username=usuari)
    except:
        raise Http404("Usuari no existeix"+usuari)

    sobres = user.sobre_set.all(); # El all me retorne tots
    template = get_template("dashboard.html")
    variables = Context({
        "username": usuari,
        "author": "Eduard i Sergio",
        "sobres": sobres
    })
    page = template.render(variables)
    return HttpResponse(page)
