from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'register/',
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        'login/',
        views.Login.as_view(),
        name='login',
    ),
    path(
        'logout/',
        views.LogoutView.as_view(),
        name='logout',
    ),
    path(
        'update/',
        views.LogoutView.as_view(),
        name='update',
    ),
    path(
        'verification/',
        views.CodeVerificationView.as_view(),
        name='verification',
    ),
]