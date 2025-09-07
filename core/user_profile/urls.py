from django.urls import include,path,reverse_lazy
from django.contrib.auth.views import LogoutView
from . import views

app_name='profile'

urlpatterns=[
    path('register/',views.signup_user.as_view(),name='register'),
    path('login/',views.login_user.as_view(),name='login'),
    path('api/v1/',include(('user_profile.api.v1.urls','api_v1'),namespace='api_v1'))
]