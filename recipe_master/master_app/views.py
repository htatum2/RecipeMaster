from django.shortcuts import render, render_to_response
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
)
from .models import Recipe
from django.shortcuts import Http404,HttpResponse, HttpResponseRedirect
from searchengine.web_search import google
import operator
from django.db.models import Q
from functools import reduce

# Create your views here.
# Class based views look for <app>/<model>_<viewtype>.html by default

def home(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'master_app/home.html', context)




class RecipeListView(ListView):
    model = Recipe
    template_name = 'master_app/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']


class RecipeDetailView(DetailView):
    model = Recipe

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['recipe_name', 
              'ingredients_list',
              'instructions', 
              'overallRating', 
              'image', 
              'mealPrepTimeMinutes']

    def form_valid(self, form):
        form.instance.recipe_creator = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'master_app/grilledCheeseNaan.html')

def profile(request):
    return HttpResponse('<h1>Awesome profile view coming soon!</h1>')

def veganrecipes(request):
    return HttpResponse('<h1>I like vegan recipes.<h1>')

def recipes(request):
    return render(request, 'master_app/recipes.html')

def search(request):
    if request.POST:
        return render_to_response('master_app/search.html', {'result': google()})
        #return HttpResponseRedirect("/")
    else:
        return render_to_response('master_app/search.html')

def veg_search(request):
    return render(request, 'master_app/veg_search.html')   


class RecipeSearchListView(RecipeListView):
    """
    Display a Blog List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self):
        result = super(RecipeSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list))
            )

        return result
