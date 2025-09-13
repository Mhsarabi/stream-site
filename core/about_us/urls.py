from django.urls import path
from . import views

app_name='about'

urlpatterns=[
    path('about',views.AboutUs.as_view(),name='about_us'),
    path('contact',views.ContactUs.as_view(),name='contact_us'),
    path('questions',views.QuestionView.as_view(),name='questions')
]