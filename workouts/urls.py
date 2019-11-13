from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add_workout, name='add_workout'),
    path('view/', views.view_workouts, name='view_workouts'),
    path('', views.visualize_data, name='visualize_data')
]
