from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from django.core.serializers.json import DjangoJSONEncoder

from .forms import WorkoutForm, CardioForm, NutritionForm, WeightForm, SleepForm
from .models import Cardio, Workout, Nutrition, Weight, Sleep


@login_required(login_url='/')
def add_workout(request):
    destinationTab = request.GET.get('dest', "destination_not_set")
    context = {'workoutForm': WorkoutForm(), 'cardioForm': CardioForm(),
               'nutritionForm': NutritionForm(), 'weightForm': WeightForm(), 'sleepForm': SleepForm(), 'destinationTab': destinationTab}
    if request.method == "POST":
        if 'workout' in request.POST:
            form = WorkoutForm(request.POST)
            if form.is_valid():
                workout = form.save(commit=False)
                workout.user = request.user
                workout.save()
                messages.success(
                    request, 'Your workout was recorded succesfully!')
            else:
                messages.error(
                    request, "There was an error recording your workout!")
        if 'cardio' in request.POST:
            form = CardioForm(request.POST)
            if form.is_valid():
                cardio = form.save(commit=False)
                cardio.user = request.user
                cardio.save()
                messages.success(
                    request, 'Your cardio was recorded succesfully!')
            else:
                messages.error(
                    request, "There was an error recording your cardio!")
        if 'nutrition' in request.POST:
            form = NutritionForm(request.POST)
            if form.is_valid():
                nutrition = form.save(commit=False)
                nutrition.user = request.user
                nutrition.autofill_macros = form.cleaned_data['autofill_macros']
                nutrition.calories = form.cleaned_data['grams_of_fat'] * 9 + \
                    form.cleaned_data['grams_of_protein'] * \
                    4 + form.cleaned_data['grams_of_carbs'] * 4
                print(form.cleaned_data['grams_of_protein'])
                nutrition.save()
                messages.success(
                    request, 'Your meal was recorded succesfully!')
            else:
                messages.error(
                    request, "There was an error recording your meal!")
        if 'wght_entry' in request.POST:
            form = WeightForm(request.POST)
            # context['weightForm'] = form
            if form.is_valid():
                weightEntry = form.save(commit=False)
                weightEntry.user = request.user
                weightEntry.save()
                messages.success(
                    request, 'Your weight was recorded succesfully!')
            else:
                messages.error(
                    request, "There was an error recording your weight!")
        if 'sleep' in request.POST:
            form = SleepForm(request.POST)
            # context['weightForm'] = form
            if form.is_valid():
                sleep = form.save(commit=False)
                sleep.user = request.user
                sleep.save()
                messages.success(
                    request, 'Your sleep was recorded succesfully!')
            else:
                messages.error(
                    request, "There was an error recording your sleep!")

    return render(request, 'workouts/addWorkout.html', context)


# if user is not logged in, redirect to home page
@login_required(login_url='/home')
def view_workouts(request):
    user = request.user
    cardio_sessions = Cardio.objects.all().filter(user=user)
    workout_sessions = Workout.objects.all().filter(user=user)
    nutrition_sessions = Nutrition.objects.all().filter(user=user)
    weight_sessions = Weight.objects.all().filter(user=user)
    context = {'workouts': workout_sessions,
               'cardios': cardio_sessions, 'calories': nutrition_sessions, 'weights': weight_sessions}
    return render(request, 'workouts/viewWorkouts.html', context)


@login_required(login_url='/home')
def visualize_data(request):
    user = request.user
    cardio = Cardio.objects.all().filter(user=user)
    workouts = Workout.objects.all().filter(user=user)
    meals = Nutrition.objects.all().filter(user=user)
    weights = Weight.objects.all().filter(user=user).order_by("date")

    context = {'meals': meals, 'workouts': workouts,
               'cardios': cardio, 'weights': weights}
    return render(request, 'workouts/visualize.html', context)


@login_required(login_url='/home')
def delete_workout(request, id):
    workout = Workout.objects.get(id=id)
    if(workout.user == request.user):
        workout.delete()
        payload = {'success': True}
    else:
        payload = {'success': False}
    return HttpResponse(json.dumps(payload), content_type='application/json')


@login_required(login_url='/home')
def delete_meal(request, id):
    meal = Nutrition.objects.get(id=id)
    if(meal.user == request.user):
        meal.delete()
        payload = {'success': True}
    else:
        payload = {'success': False}
    return HttpResponse(json.dumps(payload), content_type='application/json')


@login_required(login_url='/home')
def delete_cardio(request, id):
    cardio = Cardio.objects.get(id=id)
    if(cardio.user == request.user):
        cardio.delete()
        payload = {'success': True}
    else:
        payload = {'success': False}
    return HttpResponse(json.dumps(payload), content_type='application/json')


@login_required(login_url='/home')
def delete_weight(request, id):
    weight = Weight.objects.get(id=id)
    if(weight.user == request.user):
        weight.delete()
        payload = {'success': True}
    else:
        payload = {'success': False}
    return HttpResponse(json.dumps(payload), content_type='application/json')
