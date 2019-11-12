from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import timezone
from django.contrib.auth.decorators import login_required

from .forms import WorkoutForm, CardioForm, NutritionForm
from .models import Cardio, Workout, Nutrition

@login_required(login_url='/auth/signup')
def add_workout(request):
    context = {'workoutForm': WorkoutForm(), 'cardioForm': CardioForm(), 'nutritionForm': NutritionForm()}
    if request.method == "POST":
        print(request.POST)
        if 'workout' in request.POST:
            print("--- WORKOUT DECTECTED ---")
            form = WorkoutForm(request.POST)
            if form.is_valid():
                workout = form.save(commit=False)
                workout.user = request.user
                workout.save()
        if 'cardio' in request.POST:
            print("--- CARDIO DECTECTED ---")
            form = CardioForm(request.POST)
            if form.is_valid():
                print("VALID CARDIO")
                cardio = form.save(commit=False)
                cardio.user = request.user
                cardio.save()
            else:
                print("INVALID CARDIO")
        if 'nutrition' in request.POST:
            print("---- NURTRITION DETECTED --- ")
            form = NutritionForm(request.POST)
            if form.is_valid():
                print("VALID NUTRITION")
                nutrition = form.save(commit=False)
                nutrition.user = request.user
                nutrition.save()
            else:
                print("INVALID CALS")
    return render(request, 'workouts/addWorkout.html', context)




@login_required(login_url='/auth/signup')
def view_workouts(request):
    user = request.user
    cardio_sessions = Cardio.objects.all().filter(user=user)
    workout_sessions = Workout.objects.all().filter(user=user)
    nutrition_sessions = Nutrition.objects.all().filter(user=user)
    context = {'workouts': workout_sessions, 'cardios': cardio_sessions, 'calories': nutrition_sessions}
    return render(request, 'workouts/viewWorkouts.html', context)