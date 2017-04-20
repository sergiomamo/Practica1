from django.forms import ModelForm
from models import Books, Author


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
        exclude = ('user', 'date',)

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        exclude = ('user',)
