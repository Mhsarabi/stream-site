from django.urls import path,include
from movie import views

app_name='movie'

urlpatterns=[
    path('',views.MovieView.as_view(),name='main'),
    path('movies',views.MoviePageView.as_view(),name='movies'),
    path('series',views.SeriePageView.as_view(),name='series'),
    path('movie/<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path("series/<slug:slug>/", views.SerieDetailView.as_view(), name="series_detail"),
    path("series/<slug:series_slug>/episode/<int:episode_number>/", views.EpisodeDetailView.as_view(), name="episode_detail"),
    path("movie/<slug:slug>/download/", views.download_movie, name="download_movie"),
    path("series/<slug:series_slug>/episode/<int:episode_number>/download/", views.download_episode, name="download_episode"),
    path("download-report", views.download_report, name="download_report"),
    
]