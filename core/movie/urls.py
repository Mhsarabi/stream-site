from django.urls import path,include
from movie import views

app_name='movie'

urlpatterns=[
    path('',views.MovieView.as_view(),name='main'),
]