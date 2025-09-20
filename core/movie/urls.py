from django.urls import path,include
from movie import views

app_name='movie'

urlpatterns=[
    path('',views.MovieView.as_view(),name='main'),
    path('movies',views.MoviePageView.as_view(),name='movies'),
    path('series',views.SeriePageView.as_view(),name='series'),
    path('movie/<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail')
    
]