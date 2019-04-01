# Generated by Django 2.1.7 on 2019-04-01 03:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master_app', '0006_auto_20190331_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='date',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='user',
            new_name='recipe_creator',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='recipeCategory',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients_list',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterUniqueTogether(
            name='recipereview',
            unique_together={('recipe', 'user')},
        ),
    ]
