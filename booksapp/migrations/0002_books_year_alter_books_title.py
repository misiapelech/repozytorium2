# Generated by Django 4.2.3 on 2023-07-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, default=1970),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=70, unique=True),
        ),
    ]