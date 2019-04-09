from .models import Recipe, Review
from django import forms
import django_filters

class RecipeFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(lookup_expr='icontains')
    #Rating = django_filters.ModelMultipleChoiceFilter(queryset = RecipeReview.objects.all(), widget = forms.CheckboxSelectMultiple)
    meal_PrepTime_Minutes = django_filters.NumberFilter(lookup_expr='lt', label='Total Meal Prep/Cook Time')
    calories = django_filters.NumberFilter( lookup_expr='lt', label='Calories Less Than')
    calories_lt = django_filters.NumberFilter(lookup_expr='gt', label='Calories Greater Than')
    average_rating = django_filters.NumberFilter(lookup_expr='gt', label = 'Overall Rating')
    authenticity= django_filters.NumberFilter(lookup_expr='gt',label='Authenticity Rating')
    class Meta:
        model=Recipe
        fields = ['country', 'calories','calories','meal_PrepTime_Minutes','category', 'average_rating', 'authenticity']




