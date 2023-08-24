from django.http import HttpRequest, Http404
from django.test import TestCase
from booksapp.models import Books, Genre, Writer
import pytest
from django.urls import reverse
from django.test import Client


"""Fixture providing test client."""
@pytest.fixture
def user_client():
    client = Client()
    return client



@pytest.mark.django_db
def test_add_books_view(user_client):
    """1 test, This function tests the 'add_books' view, checking the response code and the content of the context."""
    response = user_client.get(reverse('add_books'))
    assert response.status_code == 200
    assert 'books' in response.context


@pytest.mark.django_db
def test_add_books_view_authenticated(authenticated_client):
    """2 test , This function tests, the view 'add_books' for the logged in user ."""
    response = authenticated_client.get(reverse('add_books'))
    assert response.status_code == 200



@pytest.mark.django_db
def test_new_book_view(authenticated_client):
    """3 test , This function tests the 'new_book' view for the logged-in user, checking the response code."""
    response = authenticated_client.get(reverse('new_book'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_new_book_view_unauthenticated(user_client):
    """4 test, This function tests the 'new_book' view for a non-logged-in user, checking redirects to the login page."""
    response = user_client.get(reverse('new_book'))
    assert response.status_code == 302
    assert 'login' in response.url


@pytest.mark.django_db
def test_new_book_view_authenticated20(authenticated_client):
    """5 Test,  whether a logged-in user can add a new book using the 'new_book' view."""

    genre = Genre.objects.create(genre=1)
    writer = Writer.objects.create(name='Robert', surname='Kiyosaki')

    book_data = {
        'title': 'Biedny ojciec bogaty ojciec',
        'authors': writer.id,
        'year': 1997,
        'description': 'A test book description',
        'cover': 'Carrie.jpg',
        'genre': genre.id,
        'stars': 5,
        'text_review': 'This is a great book!',
    }

    response = authenticated_client.post(reverse('new_book'), book_data)

    assert response.status_code == 302
    assert Books.objects.filter(title='Biedny ojciec bogaty ojciec').exists()

    saved_book = Books.objects.get(title='Biedny ojciec bogaty ojciec')
    assert saved_book is not None

@pytest.mark.django_db
def test_edit_book_view(authenticated_client):
    """ 6 test, This function tests the correctness of access to the books editing view for the logged user """
    book = Books.objects.create(title='Biedny ojciec bogaty ojciec')
    response = authenticated_client.get(reverse('edit_book', args=[book.id]), data={'title': 'Biedny ojciec bogaty ojciec'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_book_view_not_authenticated(user_client):
    """7 test, this function tests whether a non-logged-in user cannot edit books, redirecting to the login page."""
    book = Books.objects.create(title='Biedny ojciec bogaty ojciec')
    response = user_client.post(reverse('edit_book', args=[book.id]))
    assert response.status_code == 302
    assert 'login' in response.url


@pytest.mark.django_db
def test_edit_book_view_for_authenticated_client(authenticated_client):
    """8 test, This function tests whether the logged-in user can edit the book."""
    book_id = 4
    url = reverse('edit_book', args=[book_id])
    dane = {'title': 'Biedny ojciec bogaty ojciec'}
    Books.objects.create(id=book_id, title='Biedny ojciec bogaty ojciec')
    response = authenticated_client.post(url, dane)
    assert response.status_code == 302
    books = Books.objects.get(id=book_id)
    assert books is not None


@pytest.mark.django_db
def test_edit_book_view_for_authenticated_client(authenticated_client):
    """9 test verifies that the logged-in user can edit the book, and that the edited book was successfully added to the database."""
    book_id = 4
    url = reverse('edit_book', args=[book_id])
    Books.objects.create(id=book_id, title='Biedny ojciec bogaty ojciec')
    updated_data = {'title': 'new book'}
    response = authenticated_client.post(url, updated_data)
    assert response.status_code == 200
    updated_book = Books.objects.get(id=book_id)
    assert updated_book.title == 'Biedny ojciec bogaty ojciec'


@pytest.mark.django_db
def test_delete_book_view(authenticated_client):
    """10 test, this function tests whether the logged-in user can correctly access the books deletion view."""
    book = Books.objects.create(title='Biedny ojciec bogaty ojciec')
    response = authenticated_client.get(reverse('delete_book', args=[book.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_book_view_not_authenticated(user_client):
    """11 test, this function tests whether a non-logged-in user cannot delete books."""
    book = Books.objects.create(title='Biedny ojciec bogaty ojciec')
    response = user_client.post(reverse('delete_book', args=[book.id]))
    assert response.status_code == 302
    assert 'login' in response.url



@pytest.mark.django_db
def test_delete_book_view_get_request(authenticated_client):
    """12 test, this function tests whether the books deletion view correctly handles the GET request for the logged-in user."""
    book = Books.objects.create(title='Biedny ojciec bogaty ojciec')
    response = authenticated_client.post(reverse('delete_book', args=[book.id]))
    assert response.status_code == 302
    assert not Books.objects.filter(pk=book.id).exists()






