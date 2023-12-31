# Generated by Django 4.2.2 on 2023-06-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directores', '0002_alter_film_duration_alter_film_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='biography',
            field=models.TextField(help_text='Introduzca la biografía del director.', max_length=1000),
        ),
        migrations.AlterField(
            model_name='film',
            name='synopsis',
            field=models.TextField(help_text='Sinopsis de la película.', max_length=1000),
        ),
    ]
