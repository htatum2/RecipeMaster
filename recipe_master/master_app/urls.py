from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='master-home'),
    path('about/', views.about, name='master-about'),
    path('search/', views.search, name='master-search'),
    path('profile/', views.profile, name='master-profile'),

]