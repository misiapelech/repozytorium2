# Generated by Django 4.2.3 on 2023-08-22 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0003_remove_writer_biography_remove_writer_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='genre_literary',
            new_name='genre',
        ),
    ]
