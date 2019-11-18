from django.shortcuts import render, redirect


from workouts.models import Workout, Cardio


def home(request):
    if request.user.is_authenticated:
        if(request.GET.get('first_login', '') == 'true'):
            print("NEW")
            first_login = "true"
        else:
            print("OLD")
            first_login = "false"
        return render(request, 'home/home-authenticated.html', {'first_login': first_login})
    else:
        return render(request, 'home/home-not-authenticated.html', {})
