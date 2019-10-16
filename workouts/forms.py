from django import forms

from .models import Workout, Cardio

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('exercise_name', 'sets', 'reps', 'weight', 'sets_successful')

class CardioForm(forms.ModelForm):
    class Meta:
        model = Cardio
        fields = ('type', 'duration', 'distance_in_miles')
