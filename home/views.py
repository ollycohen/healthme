from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.db.models import Count

from workouts.models import Workout, Cardio

@login_required(login_url='/auth/signup')
def home(request):
    user = request.user
    cardio_sessions = Cardio.objects.order_by('weight').all().filter(user=user)
    workout_sessions = Workout.objects.all().filter(user=user)

    # workouts_success = Workout.objects.filter(sets_successful__lte=sets)
    workouts_unsuccessful = Workout.objects.filter(sets__gt=F('sets_successful'))
    workout_success_ratio = float(len(workout_sessions) - len(workouts_unsuccessful)) / float(len(workout_sessions))

    context = {"workouts": workout_sessions, "cardio": cardio_sessions, "workouts_unsuccessful": workouts_unsuccessful, "success_ratio": workout_success_ratio}
    return render(request, 'home/home.html', context)
