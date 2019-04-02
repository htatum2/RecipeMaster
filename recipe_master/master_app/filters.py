from .models import Recipe
import django_filters

class RecipeFilter(django_filters.FilterSet):
    #country = django_filters.CharFilter(lookup_expr='icontains')
    #meal_PrepTime_Minutes_lt = django_filters.NumberFilter(name = 'meal_PrepTime_Minutes', lookup_expr='lt')
    #calories_lt= django_filters.NumberFilter(name='calories', lookup_expr='lt')
    #calories_gt= django_filters.NumberFilter(name='calories', lookup_expr='gt')
    class Meta:
        model=Recipe
        fields = ['country', 'calories','meal_PrepTime_Minutes']




