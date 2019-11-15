from django.shortcuts import render, redirect


from workouts.models import Workout, Cardio

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/home-authenticated.html', {})
    else:
        return render(request, 'home/home-not-authenticated.html', {})
