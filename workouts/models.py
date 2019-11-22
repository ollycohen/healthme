from django.db import models
from django.contrib.auth.models import User
import datetime


class Workout(models.Model):
    exercise_name = models.CharField(max_length=50)
    sets = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    sets_successful = models.PositiveSmallIntegerField()
    date = models.DateField()

    # associate each workout with exactly one user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.exercise_name + " for " + str(self.sets) + " sets of " + str(self.reps) + " with succesful sets: " + str(self.sets_successful) + " on " + str(self.date)


class Cardio(models.Model):
    TYPES = [
        ('run', 'Running'),
        ('bike', 'Biking'),
        ('elipitical', 'Eliptical'),
        ('other', 'Other')
    ]
    date = models.DateField()

    # associate each workout with exactly one user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    type = models.CharField(choices=TYPES, max_length=15)
    duration = models.PositiveSmallIntegerField()
    distance_in_miles = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.type + " for " + str(self.duration) + " went " + str(self.distance_in_miles) + " miles on " + str(self.date)


class Nutrition(models.Model):
    food_name = models.CharField(max_length=50)
    autofill_macros = models.BooleanField()
    grams_of_protein = models.PositiveSmallIntegerField()
    grams_of_carbs = models.PositiveSmallIntegerField()
    grams_of_fat = models.PositiveSmallIntegerField()
    calories = models.PositiveSmallIntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Weight(models.Model):
    weight_entry = models.PositiveSmallIntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']
