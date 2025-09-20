from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.views import View
from .models import Movie,Series,Episode

# Create your views here.
class MovieView(ListView):
    template_name='movie/index.html'
    model=Movie

    def get_context_data(self, **kwargs):
      context=super().get_context_data(**kwargs)
      context['last_movie']=Movie.objects.last()
      context['movie_slide']=Movie.objects.filter(type='poster')
      context['movie_product']=Movie.objects.filter(type='product')
      context['movie_future']=Movie.objects.filter(type='future')
      context['movie_rating']=Movie.objects.all().order_by('rating')[:10]
      context['new_movie']=Movie.objects.last()
      context['series_slide']=Series.objects.filter(type='poster')
      context['series_future']=Series.objects.filter(type='future')



      return context
    
    def prepare_movies(self, movies):
        for movie in movies:
            full_stars = int(movie.rating)  
            half_star = 1 if (movie.rating - full_stars) >= 0.5 else 0  
            empty_stars = 5 - full_stars - half_star  
            movie.stars = {
                'full': range(full_stars),
                'half': range(half_star),
                'empty': range(empty_stars),
            }
        return movies
    

class MoviePageView(ListView):
    template_name='movie/movie-category.html'
    model=Movie

    def get_context_data(self, **kwargs):
      context=super().get_context_data(**kwargs)
      context['movie_slide']=Movie.objects.filter(type='poster')
      context['movie_product']=Movie.objects.filter(type='product')
      context['movie_future']=Movie.objects.filter(type='future')
      return context
 
    
class SeriePageView(ListView):
    template_name='movie/show-category.html'
    model=Series

    def get_context_data(self, **kwargs):
      context=super().get_context_data(**kwargs)
      context['serie_slide']=Series.objects.filter(type='poster')
      context['serie_product']=Series.objects.filter(type='product')
      context['serie_future']=Series.objects.filter(type='future')
      return context


class MovieDetailView(DetailView):
    model = Movie
    template_name ='movie/movie-details.html'
    context_object_name ='movie'
    slug_field ='slug'
    slug_url_kwarg ='slug'

    def get_context_data(self, **kwargs):
       context=super().get_context_data(**kwargs)
       context['movies']=Movie.objects.all()
       return context
    
class SerieDetailView(DetailView):
    model = Series
    template_name ='movie/series_detail.html'
    context_object_name ='serie'
    slug_field ='slug'
    slug_url_kwarg ='slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        series = self.get_object()  
        context['series'] =Series.objects.all()
        context['episodes'] =series.episodes.all()  
        return context
    
class EpisodeDetailView(View):
    template_name = 'movie/episode-detail.html'

    def get(self, request, series_slug, episode_number):
        serie = get_object_or_404(Series, slug=series_slug)
        episode = get_object_or_404(Episode, series=serie, episode_number=episode_number)

        return render(request, self.template_name, {
            "serie": serie,
            "episode": episode,
            "episodes": serie.episodes.all(), 
            "series":Series.objects.all()
        })

    
