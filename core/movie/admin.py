from django.contrib import admin
from movie.models import Movie,Actor,Genre,MovieRating,Series,SeriesRating,Episode

# Register your models here.
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(MovieRating)
admin.site.register(Series)
admin.site.register(SeriesRating)
admin.site.register(Episode)




