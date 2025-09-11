from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class StreamProducts(TemplateView):
    template_name='movie/index.html'
