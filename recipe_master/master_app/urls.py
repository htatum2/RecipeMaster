from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='master-home'),
    path('about/', views.about, name='master-about'),
    path('search/', views.search, name='master-search'),
    path('profile/', views.profile, name='master-profile'),
    path('search/', views.search, name='searchengine-search'),
    path('recipes/', views.recipes, name='master-recipes'),
    path('search/veg_search.html', views.veg_search, name='searchengine-search'),
    
]