# Generated by Django 4.0 on 2021-12-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_ebook', '0002_catalog_booklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='type_of_book',
            field=models.CharField(choices=[('Audiobook', 'Audiobook'), ('Ebooks', 'Ebooks')], default='Ebooks', max_length=10),
        ),
    ]
