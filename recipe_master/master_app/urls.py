from django.urls import path, include
from django.utils import timezone
from .models import Recipe
#from filterview import FilterView
from django.views.generic import DetailView, ListView
#from django.conf.urls import url, include
from .views import (
    #RecipeListView, 
    RecipeDetailView, 
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
    review,
    about
)
from . import views

# RecipeDetailView expects modelName_detail.html
# RecipeCreateView expects modelName_form.html


urlpatterns = [
    #path('', RecipeListView.as_view(), name='master-home'),
    path('', views.home, name='master-home'),
    #Path to Discover Recipes
    path('discover/', views.recipe_list, name='master-discover'),
    #Path to see details about a specific recipe
    path('recipe/<pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    #Path to upload a new recipe
    path('post/new/', RecipeCreateView.as_view(), name='recipe-create'),
    #Path to Update a current recipe
    path('recipe/<pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    #path to Delete a Recipe
    path('recipe/<pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),

   
   
    #TODO: Path to Create a new Review about a specific recipe
    path('recipe/<pk>/review/new/', views.add_review, name='add_review'),
    #Path to see a specific review.
    path('review/<pk>/', views.review_detail, name= 'review_detail'),
    #See a list of reviews
    path('reviews/', views.review_list, name='review_list'),
   
   
   #About RecipeMaster
    path('about/', views.about, name='master-about'),
    #User Profile
    path('profile/', views.profile, name='master-profile'),

    #path('reviews/', include('reviews.urls')),
    #path('recipes/', views.recipes,name='master-recipes'),
    
]