from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import WorkoutForm, CardioForm, NutritionForm
from .models import Cardio, Workout, Nutrition

@login_required(login_url='/auth/signup')
def add_workout(request):
    context = {'workoutForm': WorkoutForm(), 'cardioForm': CardioForm(), 'nutritionForm': NutritionForm()}
    if request.method == "POST":
        if 'workout' in request.POST:
            form = WorkoutForm(request.POST)
            if form.is_valid():
                workout = form.save(commit=False)
                workout.user = request.user
                workout.save()
                messages.success(request, 'Your workout was recorded succesfully!')
            else:
                messages.error(request, "There was an error recording your workout!")
        if 'cardio' in request.POST:
            form = CardioForm(request.POST)
            if form.is_valid():
                cardio = form.save(commit=False)
                cardio.user = request.user
                cardio.save()
                messages.success(request, 'Your cardio was recorded succesfully!')
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


@login_required(login_url='/auth/signup')
def visualize_data(request):
    user = request.user
    calories = Nutrition.objects.all().filter(user=user)
    fats = calories.all().filter(type='fat').values()
    proteins = calories.all().filter(type='protein')
    carbs = calories.all().filter(type='carb').values()
    context = {'all_cals': calories, 'fats': fats, 'proteins': proteins, 'carbs': carbs}
    return render(request, 'home/home.html', context)

