# Generated by Django 2.1.7 on 2019-04-01 23:16

from django.db import migrations
import master_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('master_app', '0009_recipe_calories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='calories',
            field=master_app.models.MinMaxFloat(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='meal_PrepTime_Minutes',
            field=master_app.models.MinMaxFloat(),
        ),
    ]
