from django import forms

from .models import Workout, Cardio, Nutrition


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('exercise_name', 'sets', 'reps',
                  'weight', 'sets_successful', 'date')


class CardioForm(forms.ModelForm):
    class Meta:
        model = Cardio
        fields = ('type', 'duration', 'distance_in_miles', 'date')


class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = ('food_name', 'grams_of_fat',
                  'grams_of_protein', 'grams_of_carbs', 'date')
