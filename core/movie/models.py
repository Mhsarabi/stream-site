from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField()
    duration = models.CharField(max_length=50)
    actors = models.CharField(max_length=255)   
    genres = models.CharField(max_length=255)

    def __str__(self):
        return self.title