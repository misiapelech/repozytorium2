# Generated by Django 4.2.3 on 2023-08-13 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0028_alter_genre_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='gatunek_literacki',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booksapp.genre'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Dramat'), (1, 'Nauka o finansach'), (2, 'Horror'), (3, 'Fantazy'), (4, 'Kryminał'), (5, 'Biografia'), (6, 'Historia'), (7, 'Popularno naukowe'), (8, 'Literatura Faktu'), (9, 'Prawo'), (10, 'Powieść')], default=0),
        ),
    ]