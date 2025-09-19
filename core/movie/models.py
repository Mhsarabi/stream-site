from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Avg


User=get_user_model()
# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Actor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    status_choices=[('poster', 'poster'),('product', 'product'),('future', 'future')]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)
    duration_minutes = models.PositiveIntegerField(help_text="مدت فیلم به دقیقه")
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")
    release_date = models.DateField(null=True, blank=True)
    poster = models.ImageField(upload_to='movies/posters/', null=True, blank=True)
    trailer = models.FileField(upload_to='movies/trailers/', null=True, blank=True)
    type=models.CharField(max_length=10,choices=status_choices,default='product')

    def __str__(self):
        return f"{self.title} ({self.release_date.year if self.release_date else 'N/A'})"
    
    def update_rating(self):
        avg_rating = self.ratings.aggregate(avg=Avg("stars"))["avg"]
        self.rating = avg_rating if avg_rating else 0
        self.save()

    def formatted_duration(self):
        hours = self.duration_minutes // 60
        minutes = self.duration_minutes % 60

        parts = []
        if hours:
            parts.append(f"{hours} ساعت")
        if minutes:
            parts.append(f"{minutes} دقیقه")

        return " و ".join(parts) if parts else "نامشخص"
    
    def actors_list(self):
        return ", ".join(actor.name for actor in self.actors.all())

    def genres_list(self):
        return " | ".join(genre.name for genre in self.genres.all())

class Series(models.Model):
    status_choices = [
        ('poster', 'poster'),
        ('product', 'product'),
        ('future', 'future')
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)
    actors = models.ManyToManyField(Actor, related_name="series")
    genres = models.ManyToManyField(Genre, related_name="series")
    release_date = models.DateField(null=True, blank=True)
    poster = models.ImageField(upload_to='series/posters/', null=True, blank=True)
    trailer = models.FileField(upload_to='series/trailers/', null=True, blank=True)
    type = models.CharField(max_length=10, choices=status_choices, default='product')

    def __str__(self):
        return f"{self.title} ({self.release_date.year if self.release_date else 'N/A'})"
    
    def update_rating(self):
        avg_rating = self.ratings.aggregate(avg=Avg("stars"))["avg"]
        self.rating = avg_rating if avg_rating else 0
        self.save()

    def formatted_duration(self):
        hours = self.duration_minutes // 60
        minutes = self.duration_minutes % 60

        parts = []
        if hours:
            parts.append(f"{hours} ساعت")
        if minutes:
            parts.append(f"{minutes} دقیقه")

        return " و ".join(parts) if parts else "نامشخص"
    
    def actors_list(self):
        return ", ".join(actor.name for actor in self.actors.all())

    def genres_list(self):
        return " | ".join(genre.name for genre in self.genres.all())


class MovieRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ratings")
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )  

    class Meta:
        unique_together = ('user', 'movie')  

    def __str__(self):
        return f"{self.user.username} rated {self.movie.title} with {self.stars} stars"
    

class SeriesRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name="ratings")
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        unique_together = ('user', 'series')

    def __str__(self):
        return f"{self.user.username} rated {self.series.title} with {self.stars} stars"
    

class Episode(models.Model):
    series = models.ForeignKey(Series, related_name="episodes", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField(help_text="مدت قسمت به دقیقه")
    episode_number = models.PositiveIntegerField()
    release_date = models.DateField(null=True, blank=True)
    poster = models.ImageField(upload_to='series/episodes/poster/', null=True, blank=True)
    video_file = models.FileField(upload_to='series/episodes/video/', null=True, blank=True)

    class Meta:
        ordering = ['episode_number']

    def __str__(self):
        return f"{self.series.title} - قسمت {self.episode_number}"