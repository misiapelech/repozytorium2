from django.urls import path
from booksapp.views import wszystkie_ksiazki, nowa_książka, edytuj_książkę, usuń_książkę

urlpatterns = [

    path('wszystkie/', wszystkie_ksiazki, name="wszystkie_ksiazki"),
    path('nowa/', nowa_książka, name="nowa_książka"),
    path('edytuj/<int:id>/', edytuj_książkę, name="edytuj_książkę"),
    path('usun/<int:id>/', usuń_książkę, name="usuń_książkę")


]
