from django.apps import AppConfig

"""Configure the 'booksapp' application."""
class BooksappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booksapp'
