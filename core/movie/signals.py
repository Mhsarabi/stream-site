from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Rating

@receiver([post_save, post_delete], sender=Rating)
def update_movie_rating(sender, instance, **kwargs):
    instance.movie.update_rating()