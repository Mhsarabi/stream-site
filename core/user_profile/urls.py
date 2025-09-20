from django.urls import include,path,reverse_lazy
from django.contrib.auth.views import LogoutView
from .views import authentication,profile

app_name='profile'

urlpatterns=[
    path('register/',authentication.RegistrationView.as_view(),name='register'),
    path('login/',authentication.login_user.as_view(),name='login'),
    path("logout/", LogoutView.as_view(next_page="/account/login/"), name="logout"),
    path("activation/confirm/<str:token>/", authentication.ActivationView.as_view(), name="activation"),
    path("reset-password/", authentication.PasswordResetRequestView.as_view(), name="password_reset"),
    path("reset-password/<str:token>/", authentication.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('profile',profile.Profile.as_view(),name='user_profile'),
    path('profile-update',profile.ProfileUpdateView.as_view(),name='profile-update')

    # path('api/v1/',include(('user_profile.api.v1.urls','api_v1'),namespace='api_v1'))
]