from django.urls import path
from booksapp.views import add_books, new_book, edit_book, delete_book

urlpatterns = [

    path('all/', add_books, name="add_books"),
    path('new/', new_book, name="new_book"),
    path('edit/<int:id>/', edit_book, name="edit_book"),
    path('delete/<int:id>/', delete_book, name="delete_book")


]
