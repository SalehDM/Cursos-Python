# Generated by Django 4.2.2 on 2023-06-20 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directores', '0003_alter_director_biography_alter_film_synopsis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='genre',
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directores.genre'),
        ),
    ]