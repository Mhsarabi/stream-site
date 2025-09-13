from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie

# Create your views here.
class StreamProducts(ListView):
    template_name='movie/index.html'
    queryset=Movie.objects.all()
    context_object_name='movie_slide'
