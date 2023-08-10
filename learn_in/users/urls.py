from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView,
    PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView,
    PasswordResetView
)
from django.urls import path

from .views import SignUp, StudentGroupDetailView, UserDetailView, UserListView

app_name = 'users-app'

authpatterns = [
    path(
        'signup/',
        SignUp.as_view(),
        name='signup'
    ),
    path(
        'login/',
        LoginView.as_view(
            template_name='auth/login.html'
        ),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(
            template_name='auth/logged_out.html'
        ),
        name='logout'
    ),
    path(
        'password-change/',
        PasswordChangeView.as_view(
            template_name='auth/password_change_form.html'
        ),
        name='password-change'
    ),
    path(
        'password-change/done/',
        PasswordChangeDoneView.as_view(
            template_name='auth/password_change_done.html'
        ),
        name='password-change-done'
    ),
    path(
        'password-reset/',
        PasswordResetView.as_view(
            template_name='auth/password_reset_form.html'
        ),
        name='password-reset-form'
    ),
    path(
        'password-reset/done/',
        PasswordResetDoneView.as_view(
            template_name='auth/password_reset_done.html'
        ),
        name='password-reset-done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='auth/password_reset_confirm.html'
        ),
        name='password-reset-confirm'
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='auth/password_reset_complete.html'
        ),
        name='password-reset-complete'
    ),
]

urlpatterns = [
    path(
        '',
        UserListView.as_view(),
        name='user-list'
    ),
    path(
        'user/<str:username>/',
        UserDetailView.as_view(),
        name='user-detail'
    ),
    path(
        'student-group/<slug:slug>/',
        StudentGroupDetailView.as_view(),
        name='student-group-detail'
    ),
]
