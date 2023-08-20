from django.http import HttpRequest, Http404
from django.test import TestCase
from booksapp.models import Books
import pytest
from django.urls import reverse
from django.test import Client


"""Fixture dostarczający klienta testowego."""
@pytest.fixture
def user_client():
    client = Client()
    return client



@pytest.mark.django_db
def test_wszystkie_ksiazki_view(user_client):
    """1 test, Ta funkcja testuje widok 'wszystkie_ksiazki', sprawdzając kod odpowiedzi i zawartość kontekstu."""
    response = user_client.get(reverse('wszystkie_ksiazki'))
    assert response.status_code == 200
    assert 'books' in response.context


@pytest.mark.django_db
def test_wszystkie_ksiazki_view_unauthenticated(authenticated_client):
    """2 test , Ta funkcja testuje, widok 'wszystkie_ksiazki' dla zalogowanego użytkownika ."""
    response = authenticated_client.get(reverse('wszystkie_ksiazki'))
    assert response.status_code == 200



@pytest.mark.django_db
def test_nowa_książka_view(authenticated_client):
    """3 test , Ta funkcja testuje widok 'nowa_książka' dla zalogowanego użytkownika, sprawdzając kod odpowiedzi."""
    response = authenticated_client.get(reverse('nowa_książka'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_nowa_książka_view_unauthenticated(user_client):
    """4 test, Ta funkcja testuje widok 'nowa_książka' dla niezalogowanego użytkownika, sprawdzając przekierowania na stronę logowania."""
    client = Client()
    response = client.get(reverse('nowa_książka'))
    assert response.status_code == 302
    assert 'login' in response.url
    response = client.post(reverse('nowa_książka'), data={'tytuł': 'New Book'})
    assert response.status_code == 302
    assert 'login' in response.url


@pytest.mark.django_db
def test_nowa_książka_view_authenticated3(authenticated_client):
    """5 test, Ta funkcja testuje, czy zalogowany użytkownik może dodać nową książkę, za pomocą widoku o nazwie 'nowa_książka'."""
    data = {
        'tytuł': 'Nowa Książka',
        'autor': 'Nowy autor',
        'rok': 'rok wydania',
        'opis': 'opis książki',
        'okładka': 'okładka',
        'gatunek_literacki': 'gatunek literacki'
    }

    response = authenticated_client.post(reverse('nowa_książka'), data)

    assert response.status_code == 200




@pytest.mark.django_db
def test_nowa_książka_view_for_authenticated_client(authenticated_client):
    """6 test, Ta funkcja testuje, czy zalogowany użytkownik może dodać nową książkę, w raz z zapisem do bazy danych."""
    url = reverse('nowa_książka')
    client = Client()
    dane = {'tytuł': 'nowa książka'}
    Books.objects.create(tytuł=dane['tytuł'])

    response = client.post(url, dane)
    assert response.status_code == 302
    books = Books.objects.get(tytuł=dane['tytuł'])
    assert books is not None

@pytest.mark.django_db
def test_edytuj_książkę_view(authenticated_client):
    """ 7 test, Ta funkcja testuje poprawność dostępu do widoku edycji książki dla zalogowanego użytkownika, """
    book = Books.objects.create(tytuł='Test Book')
    response = authenticated_client.get(reverse('edytuj_książkę', args=[book.id]), data={'tytuł': 'New Book'})
    assert response.status_code == 200



@pytest.mark.django_db
def test_edytuj_książkę_view_not_authenticated(user_client):
    """8 test, ta funkcja testuje, czy niezalogowany użytkownik nie może edytować książki, przekierowując do strony logowania."""
    book = Books.objects.create(tytuł='Existing Book')
    response = user_client.post(reverse('edytuj_książkę', args=[book.id]))
    assert response.status_code == 302
    assert 'login' in response.url

@pytest.mark.django_db
def test_edytuj_książkę_view_unauthenticated(user_client):
    """ 9 test, ta funkcja testuje, czy niezalogowany użytkownik jest poprawnie przekierowywany do strony logowania, przy próbie uzyskania dostępu do widoku edycji książki"""
    client = Client()
    book = Books.objects.create(tytuł='Existing Book')
    response = client.get(reverse('edytuj_książkę',  args=[book.id]))
    assert response.status_code == 302
    assert 'login' in response.url
    response = client.post(reverse('edytuj_książkę', args=[book.id]), data={'tytuł': 'New Book'})
    assert response.status_code == 302
    assert 'login' in response.url


@pytest.mark.django_db
def test_edytuj_książkę_view_for_authenticated_client(authenticated_client):
    """10 test, Ta funkcja testuje, czy zalogowany użytkownik może edytować książkę."""
    book_id = 4
    url = reverse('edytuj_książkę', args=[book_id])
    client = Client()
    dane = {'tytuł': 'nowa książka'}
    Books.objects.create(id=book_id, tytuł='Książka do edycji')
    response = client.post(url, dane)
    assert response.status_code == 302
    books = Books.objects.get(id=book_id)
    assert books is not None


@pytest.mark.django_db
def test_usuń_książkę_view(authenticated_client):
    """11 test, ta funkcja testuje, czy zalogowany użytkownik może poprawnie uzyskać dostęp do widoku usuwania książki."""
    book = Books.objects.create(tytuł='Existing Book')
    response = authenticated_client.get(reverse('usuń_książkę', args=[book.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_usuń_książkę_view_not_authenticated2(user_client):
    """12 test, ta funkcja testuje, czy niezalogowany użytkownik nie może usunąć książki."""
    book = Books.objects.create(tytuł='Existing Book')
    response = user_client.post(reverse('usuń_książkę', args=[book.id]))
    assert response.status_code == 302
    assert 'login' in response.url



@pytest.mark.django_db
def test_usuń_książkę_view_get_request(authenticated_client):
    """13 test, ta funkcja testuje, czy widok usuwania książki prawidłowo obsługuje żądanie GET dla zalogowanego użytkownika."""
    book = Books.objects.create(tytuł='Existing Book')
    response = authenticated_client.get(reverse('usuń_książkę', args=[book.id]))
    assert response.status_code == 200
    assert 'book' in response.context
    assert response.context['book'] == book



