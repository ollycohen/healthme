from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add_workout, name='add_workout'),
    path('view/', views.view_workouts, name='view_workouts'),
    path('visualize/', views.visualize_data, name='visualize_data'),
    path('delete/workout/<int:id>', views.delete_workout, name='delete_workout'),
    path('delete/cardio/<int:id>', views.delete_cardio, name='delete_cardio'),
    path('delete/meal/<int:id>', views.delete_meal, name='delete_meal'),
    path('delete/weight/<int:id>', views.delete_weight, name='delete_weight')
]
