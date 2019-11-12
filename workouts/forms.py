from django import forms

from .models import Workout, Cardio, Nutrition

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('exercise_name', 'sets', 'reps', 'weight', 'sets_successful')

class CardioForm(forms.ModelForm):
    class Meta:
        model = Cardio
        fields = ('type', 'duration', 'distance_in_miles')

class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = ('type', 'count')