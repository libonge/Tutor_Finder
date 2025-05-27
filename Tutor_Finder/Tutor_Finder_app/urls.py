from django.urls import path
from . import views

urlpatterns = [
path('', views.Home, name='home'),
path('register/', views.RegisterView, name='register'), # mapping urls views
path('login/', views.LoginView, name='login'),
]