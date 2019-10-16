# Generated by Django 2.2.1 on 2019-10-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardio',
            name='distance_in_miles',
            field=models.DecimalField(decimal_places=2, help_text='Distance traveled.', max_digits=4),
        ),
    ]
