from django.contrib import admin
from .models import Books, Genre, Ocena, Writer, Review

#admin.site.register(Books)
"""Konfiguracja panelu admina dla modelu Books."""
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ["tytuł", "get_autorzy"]

    def get_autorzy(self, obj):
        """Zwraca formatowaną listę autorów książki."""
        return ", ".join([str(autor) for autor in obj.autorzy.all()])
    get_autorzy.short_description = "Autorzy"
    list_filter = ("autorzy", )
    search_fields = ("tytuł", )

admin.site.register(Genre)
admin.site.register(Ocena)
admin.site.register(Review)
admin.site.register(Writer)