from django.views.generic import DetailView,UpdateView
from user_profile.models import User
from user_profile.forms import ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy


class Profile(DetailView):
    template_name='account/setting.html'
    model=User
    context_object_name='user_profile'

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password_mask'] = '*' * 10  
        return context
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'account/update_profile.html'
    success_url = reverse_lazy('profile:user_profile')  
    def get_object(self, queryset=None):
        return self.request.user 
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if form.cleaned_data.get('password'):
            update_session_auth_hash(self.request, self.object)
        return response