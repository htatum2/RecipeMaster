from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

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

'''
class RecipeManager(models.Manager):
    
    def create_recipe(self, recipe_name, overallRating, authenticityRating,
    mealPrepTimeMinutes, descriptionTags, image, content, date_posted, 
    recipe_creater):
        recipe=self.create(recipe_name=recipe_name, overallRating=overallRating, 
        authenticityRating=authenticityRating, mealPrepTimeMinutes=mealPrepTimeMinutes, 
        descriptionTags=descriptionTags, image=image, content=content, 
        date_posted=date_posted)
        return recipe
'''        

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    country = models.TextField(blank = True, null = True)
    #rating=models.FloatRangeField(min_value=1.0, max_value=5.0)
    meal_PrepTime_Minutes=models.IntegerField()
    image = models.ImageField(default='food_default.jpg', upload_to='recipe_pics')
    ingredients_list = models.TextField(max_length=500, default='')
    instructions = models.TextField(max_length=1000, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    recipe_creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('master_app:recipe_detail', kwargs={'pk': self.pk})
    
    def averageRating(self):
        reviewCount=self.recipereview_set.count()
        if not reviewCount:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in self.recipereview_set.all()])
            return ratingSum /reviewCount

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    overallRating = models.PositiveSmallIntegerField('Overall Rating (stars) ', blank=False, default = 3, choices = RATING_CHOICES)
    authenticityRating = models.PositiveSmallIntegerField('Authenticity Rating (stars) ', blank=False, default = 3, choices = RATING_CHOICES)
    comment=models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class RecipeReview(Review):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together= ("recipe", "user")

