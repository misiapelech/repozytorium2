from django.db import models


class Genre(models.Model):
    """Model przedstawiający gatunki książek."""

    Genre = [
        (0, 'Dramat'),
        (1, 'Nauka o finansach'),
        (2, 'Horror'),
        (3, 'Fantazy'),
        (4, 'Kryminał'),
        (5, 'Biografia'),
        (6, 'Historia'),
        (7, 'Popularno naukowe'),
        (8, 'Literatura Faktu'),
        (9, 'Prawo'),
        (10, 'Powieść')
    ]

    genre = models.PositiveSmallIntegerField(default=0, choices=Genre)
class Books(models.Model):
    """Model reprezentujący książki."""
    tytuł = models.CharField(max_length=70, blank=False, unique=True)
    autorzy = models.ManyToManyField('Writer')
    rok = models.PositiveSmallIntegerField(default=2000, blank=True)
    opis = models.TextField(default="")
    okładka = models.ImageField(upload_to="covers", null=True, blank=True)
    gatunek_literacki = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.tytuł_i_autorzy()

    """Funkcja ta zwraca przedstawienie obiektu książki jako tytuł i autorzy."""
    def tytuł_i_autorzy(self):
        return "{} ({})".format(self.tytuł, ", ".join([str(autor) for autor in self.autorzy.all()]))

    """Funkcja ta zwraca formatowany ciąg tytułu i autorów książki."""

class Ocena(models.Model):
    """Model przedstawiający oceny książek."""
    gwiazdki = models.PositiveSmallIntegerField(default=5, null=True, blank=True)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)


class Review(models.Model):
    """Model przedstawiający recenzje książek."""
    treść_recenzji = models.TextField(default="", blank=True)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)


class Writer(models.Model):
    """Model przedstawiający autorów książek."""
    imie = models.CharField(max_length=40)
    nazwisko = models.CharField(max_length=40)
    biografia = models.TextField(null=True, blank=True)
    zdjecie = models.ImageField(upload_to="writers", null=True, blank=True)
    książki = models.ManyToManyField(Books,blank=True )

    def __str__(self):
        return self.imie_i_nazwisko()

    """Funkcja ta zwraca reprezentację obiektu autora jako imię i nazwisko."""

    def imie_i_nazwisko(self):
        return "{} {}".format(self.imie, self.nazwisko)

    """Funkcja ta Zwraca formatowany ciąg imienia i nazwiska autora."""




