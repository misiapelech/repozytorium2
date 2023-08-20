# Generated by Django 4.2.3 on 2023-08-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0013_alter_genre_gatunek_writer_vote_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(7, 'Popularno naukowe'), (10, 'Powieść'), (5, 'Biografia'), (4, 'Kryminał'), (9, 'Prawo'), (2, 'Horror'), (3, 'Fantazy'), (6, 'Historia'), (0, 'Dramat'), (1, 'Nauka o finansach'), (8, 'Literatura Faktu')], default=0),
        ),
        migrations.AlterField(
            model_name='vote',
            name='ocena',
            field=models.PositiveSmallIntegerField(choices=[(2, ' zła'), (0, 'Nie da się czytać'), (4, 'Bardzo dobra'), (1, 'bardzo zła'), (3, 'dobra'), (5, 'Wspaniała')], default=5),
        ),
    ]
