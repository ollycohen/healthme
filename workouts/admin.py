from django.contrib import admin
from .models import Workout, Cardio
# Register your models here.


# Registering these models to be tested within admin console
admin.site.register(Workout)
admin.site.register(Cardio)
