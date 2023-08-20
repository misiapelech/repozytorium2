from django.forms import ModelForm
from .models import Books, Genre, Ocena, Review

"""Formularz modelu Books."""
class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['tytuł','autorzy', 'rok',  'opis', 'okładka']

"""Formularz modelu Genre."""
class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']

"""Formularz modelu Ocena."""
class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['gwiazdki']
        required = {'gwiazdki': False}

"""Formularz modelu Review."""
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['treść_recenzji']
        required = {'treść_recenzji': False}