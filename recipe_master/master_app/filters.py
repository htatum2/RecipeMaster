from .models import Recipe, Review
from django import forms
import django_filters

class RecipeFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(lookup_expr='icontains')
    #Rating = django_filters.ModelMultipleChoiceFilter(queryset = RecipeReview.objects.all(), widget = forms.CheckboxSelectMultiple)
    meal_PrepTime_Minutes = django_filters.NumberFilter(lookup_expr='lt')
    calories = django_filters.NumberFilter( lookup_expr='lt')
    calories = django_filters.NumberFilter(lookup_expr='gt')
    class Meta:
        model=Recipe
        fields = ['country', 'calories','meal_PrepTime_Minutes','category']




