from django.db import models

class Writer(models.Model):
    """A model representing book authors."""
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    #written_books = models.ManyToManyField('Books', related_name='authors_written', related_query_name='author_written')

    def __str__(self):
        return self.name_and_surname()

    def name_and_surname(self):
        return "{} {}".format(self.name, self.surname)

class Genre(models.Model):
    """A model showing the genres of books."""

    Genre = [
        (0, 'Drama'),
        (1, 'Finance science'),
        (2, 'Horror'),
        (3, 'Fantasy'),
        (4, 'Criminal'),
        (5, 'Biography'),
        (6, 'History'),
        (7, 'Popularly scientific'),
        (8, 'Non-fiction'),
        (9, 'Law'),
        (10, 'Novel')
    ]

    genre = models.PositiveSmallIntegerField(default=0, choices=Genre)

class Books(models.Model):
    """Model representing books."""
    title = models.CharField(max_length=70, blank=False, unique=True)
    authors = models.ManyToManyField(Writer, related_name='books_authored', related_query_name='book_authored')
    year = models.PositiveSmallIntegerField(default=2000, blank=True)
    description = models.TextField(default="")
    cover = models.ImageField(upload_to="covers", null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title_and_authors()

    def title_and_authors(self):
        return "{} ({})".format(self.title, ", ".join([str(autor) for autor in self.authors.all()]))

class Rating(models.Model):
    """Model showing book ratings."""
    stars = models.PositiveSmallIntegerField(default=5, null=True, blank=True)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)

class Review(models.Model):
    """Model showing book reviews."""
    text_review = models.TextField(default="", blank=True)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
