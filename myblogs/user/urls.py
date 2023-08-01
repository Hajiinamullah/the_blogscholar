from django.contrib import admin
from django.urls import path,include
from . import views
from .views import sign_up,user_login

from django.contrib.auth import views as auth_views


app_name= 'user'
urlpatterns = [
    path('profile', views.user_profile, name='user_profile'),
    path('', sign_up, name='signup'),
    path('signup_success/', views.signup_success, name='signup_success'),
    path('login/', user_login, name='login_user'),
    # path('email/', views.email, name='email'),
    path('resetpassword/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name='resetpassword'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='reset_password_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='reset_password_confirm'),
]
