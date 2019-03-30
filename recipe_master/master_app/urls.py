from django.urls import path, include
from django.conf.urls import url, include
from .views import RecipeListView, RecipeDetailView
from . import views

urlpatterns = [
    path('', RecipeListView.as_view(), name='master-home'),
    url(r'(?P<pk>\d+)$', RecipeDetailView.as_view(), name = 'recipe_detail'),
    #path('recipe/<pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('about/', views.about, name='master-about'),
    path('search/', views.search, name='master-search'),
    path('profile/', views.profile, name='master-profile'),
    path('search/', views.search,name='searchengine-search'),
    path('recipes/', views.recipes,name='master-recipes'),
    path('search/veg_search.html', views.veg_search, name='searchengine-search'),
]