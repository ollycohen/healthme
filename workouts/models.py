from django.db import models
from django.contrib.auth.models import User
import datetime

class Workout(models.Model):
    exercise_name = models.CharField(max_length = 50, help_text="The name of the workout you did.")
    sets = models.PositiveSmallIntegerField(help_text="The number of sets you attempted.")
    reps = models.PositiveSmallIntegerField(help_text="The number of reps you attempted for each set.")
    success = models.BooleanField(help_text="Did you hit your sets and reps?")
    date = models.DateTimeField(help_text="Date of exercise.", auto_now_add=True)

    # associate each workout with exactly one user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
       return self.exercise_name + " for " + self.sets + " sets of " + self.reps + " was succesful: " + self.success + " on " + self.date


class Cardio(models.Model):
    TYPES = [
        ('run', 'Running'),
        ('bike', 'Biking'),
        ('elipitical', 'Eliptical'),
        ('other', 'Other')
    ]

    type = models.CharField(choices=TYPES, max_length=15, help_text="The type of cardio you did.")
    duration = models.PositiveSmallIntegerField(help_text="How long you performed this cardio for.")
    distance_in_miles= models.DecimalField(max_digits=2, decimal_places=2, help_text="Distance traveled.")
    date = models.DateTimeField(help_text="Date of exercise.", auto_now_add=True)

    # associate each workout with exactly one user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str(self):
        return self.type + " for " + self.duration + " went " + self.distance_in_miles + " miles"  + self.date