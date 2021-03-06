# The views used below are normally mapped in the AdminSite instance.
# This URLs file is used to provide a reliable view deployment for test purposes.
# It is also provided as a convenience to those who want to deploy these URLs
# elsewhere.

from django.contrib.auth import views
from . import views as account_views
from django.urls import path, re_path

urlpatterns = [
    path('profile/', account_views.Profile.as_view(), name='profile'),
    path('signup/', account_views.SignUp, name='signup'),
    path('login/', account_views.Login.as_view(), name='login',
    kwargs={'redirect_authenticated_user': True}),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('feedback/', account_views.Feedback.as_view(), name='feedback'),
    
    

    # User Change Password
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # User Reset Password
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
