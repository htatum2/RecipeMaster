from django.forms import ModelForm, Textarea
from .models import Recipe, Review

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude= ('user','date',)



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'rating', 'authenticityRating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }