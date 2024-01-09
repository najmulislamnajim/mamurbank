from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.UserRegistrationView.as_view(),name='register'),
    path('login/',views.LogInView.as_view(),name='login'),
    path('logout/',views.LogOutView.as_view(),name='logout'),
    path('profile/',views.UserBankAccountUpdateView.as_view(),name='profile'),
]
