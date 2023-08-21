from django.contrib import admin
from .models import Books, Genre, Rating, Writer, Review

#admin.site.register(Books)
"""Admin panel configuration for Books model."""
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ["title", "get_authors"]

    def get_authors(self, obj):
        """Returns a formatted list of books authors."""
        return ", ".join([str(autor) for autor in obj.authors.all()])
    get_authors.short_description = "authors"
    list_filter = ("authors", )
    search_fields = ("title", )

admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(Writer)