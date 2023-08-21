from django.http import HttpRequest, Http404
from django.test import TestCase
from booksapp.models import Books
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
    client = Client()
    response = client.get(reverse('new_book'))
    assert response.status_code == 302
    assert 'login' in response.url
    response = client.post(reverse('new_book'), data={'title': 'New Book'})
    assert response.status_code == 302
    assert 'login' in response.url


@pytest.mark.django_db
def test_new_book_view_authenticated3(authenticated_client):
    """5 test, This function tests whether a logged-in user can add a new book, using a view named 'new_book'."""
    data = {
        'title': 'new book',
        'author': 'New author',
        'year': 'year',
        'description': 'description books',
        'cover': 'cover',
        'genre_literary': 'genre literary'
    }

    response = authenticated_client.post(reverse('new_book'), data)

    assert response.status_code == 200
    book_exists = Books.objects.all().exists()
    assert book_exists is False




@pytest.mark.django_db
def test_new_book_view_for_authenticated_client(authenticated_client):
    """6 test, This function tests whether the logged-in user can add a new book, at the same time as writing to the database."""
    url = reverse('new_book')
    client = Client()
    dane = {'title': 'new book'}
    Books.objects.create(title=dane['title'])

    response = client.post(url, dane)
    assert response.status_code == 302
    books = Books.objects.get(title=dane['title'])
    assert books is not None

@pytest.mark.django_db
def test_edit_book_view(authenticated_client):
    """ 7 test, This function tests the correctness of access to the books editing view for the logged user """
    book = Books.objects.create(title='Test Book')
    response = authenticated_client.get(reverse('edit_book', args=[book.id]), data={'title': 'New Book'})
    assert response.status_code == 200



@pytest.mark.django_db
def test_edit_book_view_not_authenticated(user_client):
    """8 test, this function tests whether a non-logged-in user cannot edit books, redirecting to the login page."""
    book = Books.objects.create(title='Existing Book')
    response = user_client.post(reverse('edit_book', args=[book.id]))
    assert response.status_code == 302
    assert 'login' in response.url

@pytest.mark.django_db
def test_edit_book_view_unauthenticated(user_client):
    """ 9 test, this function tests whether a non-logged-in user is correctly redirected to the login page, when trying to access the edit view books"""
    client = Client()
    book = Books.objects.create(title='Existing Book')
    response = client.get(reverse('edit_book',  args=[book.id]))
    assert response.status_code == 302
    assert 'login' in response.url
    response = client.post(reverse('edit_book', args=[book.id]), data={'title': 'New Book'})
    assert response.status_code == 302
    assert 'login' in response.url


@pytest.mark.django_db
def test_edit_book_view_for_authenticated_client(authenticated_client):
    """10 test, This function tests whether the logged-in user can edit the book."""
    book_id = 4
    url = reverse('edit_book', args=[book_id])
    client = Client()
    dane = {'title': 'new book'}
    Books.objects.create(id=book_id, title='book for edition')
    response = client.post(url, dane)
    assert response.status_code == 302
    books = Books.objects.get(id=book_id)
    assert books is not None


@pytest.mark.django_db
def test_edit_book_view_for_authenticated_client(authenticated_client):
    """Test sprawdza, czy zalogowany użytkownik może edytować książkę, oraz czy edytowana książka pomyślnie została dodana do bazy danych."""
    book_id = 4
    url = reverse('edit_book', args=[book_id])
    book = Books.objects.create(id=book_id, title='new book')
    updated_data = {'title': 'new book'}
    response = authenticated_client.post(url, updated_data)
    assert response.status_code == 200
    updated_book = Books.objects.get(id=book_id)
    assert updated_book.title == 'new book'


@pytest.mark.django_db
def test_delete_book_view(authenticated_client):
    """11 test, this function tests whether the logged-in user can correctly access the books deletion view."""
    book = Books.objects.create(title='Existing Book')
    response = authenticated_client.get(reverse('delete_book', args=[book.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_book_view_not_authenticated2(user_client):
    """12 test, this function tests whether a non-logged-in user cannot delete books."""
    book = Books.objects.create(title='Existing Book')
    response = user_client.post(reverse('delete_book', args=[book.id]))
    assert response.status_code == 302
    assert 'login' in response.url



@pytest.mark.django_db
def test_delete_book_view_get_request(authenticated_client):
    """13 test, this function tests whether the books deletion view correctly handles the GET request for the logged-in user."""
    book = Books.objects.create(title='Existing Book')
    response = authenticated_client.post(reverse('delete_book', args=[book.id]))
    assert response.status_code == 302
    assert not Books.objects.filter(pk=book.id).exists()

