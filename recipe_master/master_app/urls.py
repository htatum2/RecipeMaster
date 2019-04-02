from django.urls import path, include
from django.utils import timezone
from .models import Recipe
#from filterview import FilterView
from django.views.generic import DetailView, ListView
#from django.conf.urls import url, include
from .views import (
    RecipeListView, 
    RecipeDetailView, 
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
    review
)
from . import views

# RecipeDetailView expects modelName_detail.html
# RecipeCreateView expects modelName_form.html


urlpatterns = [
    #path('', RecipeListView.as_view(), name='master-home'),
    path('', views.home, name='master-home'),

    #Path to see details about a specific recipe
    path('recipe/<pk>/', RecipeDetailView.as_view(), name='recipe-detail'),

    #Path to upload a new recipe
    path('post/new/', RecipeCreateView.as_view(), name='recipe-create'),

    #Path to Update a current recipe
    path('recipe/<pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),

    path('recipe/<pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),

    #TODO: Path to Create a new Review about a specific recipe
    path('recipe/<pk>/reviews/new', views.review, name='review-new'),

    path('about/', views.about, name='master-about'),
    path('search/', views.recipe_list),
    #path('search/', views.RecipeSearchListView, name='RecipeSearch'),
    path('profile/', views.profile, name='master-profile'),
    #path('search/', views.search,name='searchengine-search'),
    path('recipes/', views.recipes,name='master-recipes'),
    path('discover/', views.discover, name='master-discover'),
    path('search/veg_search.html', views.veg_search, name='searchengine-search'),
]