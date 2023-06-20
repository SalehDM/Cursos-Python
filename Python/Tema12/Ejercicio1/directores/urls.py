from django.urls import path
from.import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('director/<pk>', views.DirectorView.as_view(), name='datail_director'),
    path('film/<pk>', views.FilmView.as_view(), name='detail_film'),
]