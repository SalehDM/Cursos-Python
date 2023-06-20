from django.db import models



class Genre(models.Model):
    genreFilm=models.CharField(max_length=64,help_text='Introduzca el género de la pelicula.')

    def __str__(self):
        return self.genreFilm
    
class Film(models.Model):
    title=models.CharField(max_length=64,help_text='Introduzca el nombre de la película.')
    director=models.ForeignKey('Director',on_delete=models.SET_NULL, null=True)
    genre=models.ManyToManyField('Genre',help_text='Seleccione uno o varios géneros.')
    year=models.IntegerField(help_text='Introduzca el año que se estrenó')
    duration=models.IntegerField(help_text='Introduzca los minutos que dura la película')
    synopsis=models.TextField(max_length=1000,help_text='Sinopsis de la película.')

    def __str__(self):
        return self.title

class Director(models.Model):
    name=models.CharField(max_length=64,help_text='Introduzca el nombre del director.')
    biography=models.TextField(max_length=1000,help_text='Introduzca la biografía del director.')
       
    def __str__(self):
        return self.name