from django.forms import ModelForm
from .models import Books, Genre, Rating, Review

"""This is the Books model form."""
class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title','authors', 'year',  'description', 'cover']

"""This is the Genre Model Form."""
class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']

"""This is the Rating Model Form."""
class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['stars']
        required = {'stars': False}

"""This is the Review Model Form."""
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text_review']
        required = {'text_review': False}