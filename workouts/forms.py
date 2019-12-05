from django import forms

from .models import Workout, Cardio, Nutrition, Weight


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ('weight_entry', 'date')


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('exercise_name', 'sets', 'reps',
                  'weight_in_pounds', 'sets_successful', 'date')


class CardioForm(forms.ModelForm):
    class Meta:
        model = Cardio
        fields = ('type', 'duration_in_minutes', 'distance_in_miles', 'date')


class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = ('food_name', 'autofill_macros', 'grams_of_fat',
                  'grams_of_protein', 'grams_of_carbs', 'date')
        # widgets = {
        #     'food_name': forms.TextInput(attrs={
        #         'id': 'recipe-query'
        #     }),
        #     'autofill_macros': forms.CheckboxInput(attrs={
        #         'id': 'should-query'
        #     }),
        #     'grams_of_fat': forms.TextInput(attrs={
        #         'id': 'fat-query'
        #     }),
        #     'grams_of_protein': forms.TextInput(attrs={
        #         'id': 'protein-query'
        #     }),
        #     'grams_of_carbs': forms.TextInput(attrs={
        #         'id': 'carbs-query'
        #     })
        # }
