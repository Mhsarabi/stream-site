from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import MovieRating,SeriesRating

@receiver([post_save, post_delete], sender=MovieRating)
def update_movie_rating(sender, instance, **kwargs):
    instance.movie.update_rating()

@receiver([post_save, post_delete], sender=SeriesRating)
def update_movie_rating(sender, instance, **kwargs):
    instance.movie.update_rating()