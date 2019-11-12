from django.contrib import admin
from .models import Workout, Cardio, Nutrition
# Register your models here.


# Registering these models to be tested within admin console
admin.site.register(Workout)
admin.site.register(Cardio)
admin.site.register(Nutrition)
