from django.shortcuts import render, get_object_or_404, redirect

import books
from .models import Books, Genre, Rating, Review, Writer
from .forms import BooksForm, GenreForm, RatingForm, ReviewForm
from django.contrib.auth.decorators import login_required


def add_books(request):
    """ This function displays all books."""
    all = Books.objects.all()
    return render(request, 'books.html', {'books': all})

@login_required
def new_book(request):
    """This function supports the creation of a new books."""

    form_book = BooksForm(request.POST or None, request.FILES or None)
    form_genre = GenreForm(request.POST or None)
    form_rating = RatingForm(request.POST or None)
    form_review = ReviewForm(request.POST or None)

    if all((form_book.is_valid(), form_genre.is_valid(), form_rating.is_valid(), form_review.is_valid())):
        book = form_book.save(commit=False)
        genre = form_genre.save()
        book.genre = genre
        book.save()
        form_book.save_m2m()

        rating = form_rating.save(commit=False)
        rating.books = book
        rating.save()

        review = form_review.save(commit=False)
        review.books = book
        review.save()

        return redirect(add_books)

    return render(request, 'book_form.html', {'form': form_book, 'form_genre': form_genre, 'form_rating': form_rating, 'form_review': form_review, 'new': True})


@login_required
def edit_book(request, id):
    """This function supports editing books with the specified ID."""
    book = get_object_or_404(Books, pk=id)
    ratings = Rating.objects.filter(books=book)
    review = Review.objects.filter(books=book)

    try:
        genre = Genre.objects.get(books=book.id)
    except Genre.DoesNotExist:
        genre = None

    form_book = BooksForm(request.POST or None, request.FILES or None, instance=book)
    form_genre = GenreForm(request.POST or None, instance=genre)
    form_rating = RatingForm(request.POST or None)
    form_review = ReviewForm(request.POST or None)

    if request.method == 'POST':
        if 'stars' in request.POST:
            rating = form_rating.save(commit=False)
            rating.books = book
            rating.save()

    if request.method == 'POST':
        if 'text_review' in request.POST:
            review = form_review.save(commit=False)
            review.books = book
            review.save()

    if all((form_book.is_valid(), form_genre.is_valid(), form_rating.is_valid(), form_review.is_valid())):
        book = form_book.save(commit=False)
        genre = form_genre.save()
        book.genre = genre
        book.save()
        form_book.save_m2m()

        return redirect(add_books)

    return render(request, 'book_form.html', {'form': form_book, 'book':book,
    'form_genre': form_genre, 'ratings': ratings, 'form_rating': form_rating, 'review': review, 'form_review': form_review, 'new': False})

@login_required
def delete_book(request, id):
    """This function supports the deletion of books with the specified ID."""
    book = get_object_or_404(Books, pk=id)

    if request.method == "POST":
        book.delete()
        return redirect(add_books)


    return render(request, 'confirm.html', {'book': book})
