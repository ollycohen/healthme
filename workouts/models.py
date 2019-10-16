from django.db import models
from django.contrib.auth.models import User
import datetime

class Workout(models.Model):
    exercise_name = models.CharField(max_length = 50, help_text="The name of the workout you did.")
    sets = models.PositiveSmallIntegerField(help_text="The number of sets you attempted.")
    reps = models.PositiveSmallIntegerField(help_text="The number of reps you attempted for each set.")
    weight = models.PositiveSmallIntegerField(help_text="The weight that you attempted.")
    sets_successful = models.PositiveSmallIntegerField(help_text="The number of sets you completed succesfuly.")
    date = models.DateTimeField(help_text="Date of exercise.", auto_now_add=True)

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
    date = models.DateTimeField(help_text="Date of exercise.", auto_now_add=True)

    # associate each workout with exactly one user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    type = models.CharField(choices=TYPES, max_length=15, help_text="The type of cardio you did.")
    duration = models.PositiveSmallIntegerField(help_text="How long you performed this cardio for.")
    distance_in_miles= models.DecimalField(max_digits=4, decimal_places=2, help_text="Distance traveled.")


    def __str__(self):
        return self.type + " for " + str(self.duration) + " went " + str(self.distance_in_miles) + " miles on "  + str(self.date)
