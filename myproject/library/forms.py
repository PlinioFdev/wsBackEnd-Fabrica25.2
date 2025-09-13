from django import forms
from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'country', 'country_code']
        widgets = {
            'country': forms.TextInput(attrs={'placeholder': 'Nome do país (opcional)'}),
            'country_code': forms.TextInput(attrs={'placeholder': 'Código do país ISO (ex: BR)'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'published_year', 'isbn']
