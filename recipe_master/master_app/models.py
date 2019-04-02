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

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='')
    category_choices = ((1, 'Vegan'), (2, 'Keto'), (3, 'Paleo'), (4, 'Vegetarian'), (5, 'General'))
    category = models.PositiveSmallIntegerField('Category', blank=False, default = 5, choices = category_choices)
    description = models.CharField(max_length=200, default='')
    calories = MinMaxFloat(min_value=0.0, max_value=10000.0, default=0.0)
    meal_PrepTime_Minutes= MinMaxFloat(min_value=5.0, max_value=10000.0)
    image = models.ImageField(default='food_default.jpg', upload_to='recipe_pics')
    ingredients_list = models.TextField(max_length=500, default='')
    instructions = models.TextField(max_length=1000, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    recipe_creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})
    
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



