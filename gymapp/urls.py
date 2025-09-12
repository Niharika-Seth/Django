# Add urls based on the services in models.py
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),  # homepage
  path('plans/', views.plan_list, name='plan_list'),
  path('trainers/', views.trainer_list, name='trainer_list'),
  path('members/', views.member_list, name='member_list'),
  path('members/register/', views.member_register, name='member_register'),  # Registration
]

