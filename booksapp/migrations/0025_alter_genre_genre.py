# Generated by Django 4.2.3 on 2023-08-13 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0024_alter_genre_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(5, 'Biografia'), (10, 'Powieść'), (4, 'Kryminał'), (7, 'Popularno naukowe'), (6, 'Historia'), (0, 'Dramat'), (8, 'Literatura Faktu'), (1, 'Nauka o finansach'), (9, 'Prawo'), (3, 'Fantazy'), (2, 'Horror')], default=0),
        ),
    ]
