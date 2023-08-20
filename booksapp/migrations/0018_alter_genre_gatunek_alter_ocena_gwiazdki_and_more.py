# Generated by Django 4.2.3 on 2023-08-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0017_rename_vote_ocena_rename_książka_review_books_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Kryminał'), (2, 'Horror'), (6, 'Historia'), (1, 'Nauka o finansach'), (8, 'Literatura Faktu'), (0, 'Dramat'), (7, 'Popularno naukowe'), (3, 'Fantazy'), (9, 'Prawo'), (5, 'Biografia'), (10, 'Powieść')], default=0),
        ),
        migrations.AlterField(
            model_name='ocena',
            name='gwiazdki',
            field=models.PositiveSmallIntegerField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='książki',
            field=models.ManyToManyField(blank=True, to='booksapp.books'),
        ),
    ]
