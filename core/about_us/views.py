from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ContactMessage,Question
from .forms import ContactForm

# Create your views here.
class AboutUs(TemplateView):
    template_name='about_us/about-us.html'

class ContactUs(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'about_us/contact.html'
    success_url = reverse_lazy('about:contact_us')

    def form_valid(self, form):
        messages.success(self.request, "پیام شما با موفقیت ارسال شد ✅")
        return super().form_valid(form)
    
class QuestionView(ListView):
    template_name='about_us/questions.html'
    queryset=Question.objects.all()
    context_object_name='questions'