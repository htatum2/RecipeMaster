from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# You must save the file and run python manage.py makemigrations 
# for changes to take effect

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    recipe_creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe_name 
