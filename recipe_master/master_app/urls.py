from django.urls import path, include
#from django.conf.urls import url, include
from .views import (
    RecipeListView, 
    RecipeDetailView, 
    RecipeCreateView
)
from . import views

# RecipeDetailView expects modelName_detail.html
# RecipeCreateView expects modelName_form.html

urlpatterns = [
    path('', RecipeListView.as_view(), name='master-home'),
    path('recipe/<pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('post/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('about/', views.about, name='master-about'),
    path('search/', views.search, name='master-search'),
    path('profile/', views.profile, name='master-profile'),
    path('search/', views.search,name='searchengine-search'),
    path('recipes/', views.recipes,name='master-recipes'),
    path('search/veg_search.html', views.veg_search, name='searchengine-search'),
]