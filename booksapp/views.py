from django.shortcuts import render, get_object_or_404, redirect

import books
from .models import Books, Genre, Ocena, Review
from .forms import BooksForm, GenreForm, OcenaForm, ReviewForm
from django.contrib.auth.decorators import login_required

def wszystkie_ksiazki(request):
    """ Funkcja ta wyświetla wszystkie książki."""
    wszystkie = Books.objects.all()
    return render(request, 'books.html', {'books': wszystkie})

@login_required
def nowa_książka(request):
    """Funkcja ta obsługuje tworzenie nowej książki."""
    form_book = BooksForm(request.POST or None, request.FILES or None)
    form_genre = GenreForm(request.POST or None)
    form_ocena = OcenaForm(request.POST or None)
    form_review = ReviewForm(request.POST or None)

    if all((form_book.is_valid(), form_genre.is_valid(), form_ocena.is_valid(), form_review.is_valid())):
        book = form_book.save(commit=False)
        genre = form_genre.save()
        book.gatunek_literacki = genre
        book.save()
        form_book.save_m2m()

        ocena = form_ocena.save(commit=False)
        ocena.books = book
        ocena.save()


        review = form_review.save(commit=False)
        review.books = book
        review.save()

        return redirect(wszystkie_ksiazki)


    return render(request, 'book_form.html', {'form': form_book, 'form_genre': form_genre, 'form_ocena': form_ocena, 'form_review': form_review, 'nowa': True})

@login_required
def edytuj_książkę(request, id):
    """Funkcja ta obsługuje edycję książki o podanym ID."""
    book = get_object_or_404(Books, pk=id)
    oceny = Ocena.objects.filter(books=book)
    review = Review.objects.filter(books=book)

    try:
        genre = Genre.objects.get(books=book.id)
    except Genre.DoesNotExist:
        genre = None

    form_book = BooksForm(request.POST or None, request.FILES or None, instance=book)
    form_genre = GenreForm(request.POST or None, instance=genre)
    form_ocena = OcenaForm(request.POST or None)
    form_review = ReviewForm(request.POST or None)

    if request.method == 'POST':
        if 'gwiazdki' in request.POST:
            ocena = form_ocena.save(commit=False)
            ocena.books = book
            ocena.save()


    if request.method == 'POST':
        if 'treść_recenzji' in request.POST:
            review = form_review.save(commit=False)
            review.books = book
            review.save()

    if all((form_book.is_valid(), form_genre.is_valid(), form_ocena.is_valid(), form_review.is_valid())):
        book = form_book.save(commit=False)
        genre = form_genre.save()
        book.gatunek_literacki = genre
        book.save()
        form_book.save_m2m()

        return redirect(wszystkie_ksiazki)

    return render(request, 'book_form.html', {'form': form_book, 'book':book,
    'form_genre': form_genre, 'oceny': oceny, 'form_ocena': form_ocena, 'review': review, 'form_review': form_review, 'nowa': False})

@login_required
def usuń_książkę(request, id):
    """Funkcja ta obsługuje usuwanie książki o podanym ID."""
    book = get_object_or_404(Books, pk=id)

    if request.method == "POST":
        book.delete()
        return redirect(wszystkie_ksiazki)


    return render(request, 'potwierdz.html', {'book': book})
