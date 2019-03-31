from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# You must save the file and run python manage.py makemigrations 
# for changes to take effect
class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)

class RecipeManager(models.Manager):
    
    def create_recipe(self, recipe_name, overallRating, authenticityRating,
    mealPrepTimeMinutes, descriptionTags, image, content, date_posted, 
    recipe_creater):
        recipe=self.create(recipe_name=recipe_name, overallRating=overallRating, 
        authenticityRating=authenticityRating, mealPrepTimeMinutes=mealPrepTimeMinutes, 
        descriptionTags=descriptionTags, image=image, content=content, 
        date_posted=date_posted)
        return recipe
        
    """
    def create_recipe(self, recipe_name, overallRating, authenticityRating,
    mealPrepTimeMinutes):
        recipe=self.create(recipe_name=recipe_name, overallRating=overallRating, 
        authenticityRating=authenticityRating, mealPrepTimeMinutes=mealPrepTimeMinutes)
        return recipe
    """    

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    #rating=models.FloatRangeField(min_value=1.0, max_value=5.0)
    overallRating = MinMaxFloat(min_value=0.0, max_value=5.0)
    authenticityRating = MinMaxFloat(min_value=0.0, max_value=5.0)
    mealPrepTimeMinutes=models.IntegerField(1)
    recipeCategory = models.CharField(max_length=15)
    #diettype = models.CharField(max_length=10)
    #tags=models.ManyToManyField(String)
    descriptionTags = []
    image = models.ImageField(default='food_default.jpg', upload_to='recipe_pics')
    content = models.TextField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    recipe_creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe_name + " Rating = " + str(self.overallRating)
