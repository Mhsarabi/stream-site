from django.contrib import admin
from movie.models import Movie,Actor,Genre,Rating

# Register your models here.
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Rating)


