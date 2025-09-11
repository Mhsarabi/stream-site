from django.urls import include,path,reverse_lazy
from django.contrib.auth.views import LogoutView
from . import views

app_name='profile'

urlpatterns=[
    path('register/',views.RegistrationView.as_view(),name='register'),
    path('login/',views.login_user.as_view(),name='login'),
    path("logout/", LogoutView.as_view(next_page="/account/login/"), name="logout"),
    path("reset-password/", views.PasswordResetRequestView.as_view(), name="password_reset"),
    path("reset-password/<str:token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('api/v1/',include(('user_profile.api.v1.urls','api_v1'),namespace='api_v1'))
]