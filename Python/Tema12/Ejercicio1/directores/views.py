from django.views import generic
from .models import Director, Film

class IndexView(generic.ListView):
    template_name = 'index.html'
    model = Director

class DirectorView(generic.DetailView):
    template_name = 'director.html'
    model = Director
    
    
    """
    def get_context_data(self, **kwargs):
        context=super(FilmView,self).get_context_data(**kwargs)
        context['genero']=Film.objects.all()
        return context
    def get_context_data(self, **kwargs):
        context=super(DirectorView,self).get_context_data(**kwargs)
        context['film_list']=Film.objects.all
        return super().get_context_data(**kwargs)
    context_object_name=Director
    """

class FilmView(generic.DetailView):
    template_name = 'film.html'
    model = Film
    
    def get_context_data(self, **kwargs):
        context=super(FilmView,self).get_context_data(**kwargs)
        context['genero']=Film.objects.all()
        return context
    

