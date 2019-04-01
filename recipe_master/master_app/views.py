from django.shortcuts import render, render_to_response
from .forms import RecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView
)
from .models import Recipe
from .filters import RecipeFilter
from django.core.exceptions import PermissionDenied
from django.shortcuts import Http404,HttpResponse, HttpResponseRedirect
from searchengine.web_search import google
from django.contrib.auth.decorators import login_required
import operator
from django.utils.decorators import method_decorator
from django.db.models import Q
from functools import reduce

# Create your views here.
# Class based views look for <app>/<model>_<viewtype>.html by default

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckOwner(object):
    def get_object(self, *args, **kwargs):
        obj=super(CheckOwner, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj
class LogInBeforeChanging(LoginRequiredMixin, CheckOwner, UpdateView):
    template_name ='master_app/form.html'

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
    template_name='master_app/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView,self).get_context_data(**kwargs)
        context['RATING_CHOICES']=RecipeReview.RATING_CHOICES
        return context

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'master_app/form.html'
    form_class = RecipeForm
    fields = ['recipe_name', 
             'ingredients_list',
             'instructions', 
             'overallRating', 
             'image', 
             'mealPrepTimeMinutes']

    def form_valid(self, form):
        form.instance.recipe_creator = self.request.user
        return super(RecipeCreateView, self).form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.recipe_creator:
            return True
        return False

@login_required
def review(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if RecipeReview.objects.filter(recipe=recipe, user=request.user).exists():
        RecipeReview.objects.get(recipe=recipe, user=request.user).delete()
    valid_review = RecipeReview(
        overallRating=request.POST['overallRating'],
        authenticityRating=request.POST['authenticityRating'],
        comment=request.POST['comment'],
        user=request.user,
        recipe=recipe)
    valid_review.save()
    return HttpResponseRedirect(reverse('master_app:recipe_detail', args=(recipe.id,)))



def about(request):
    return render(request, 'master_app/grilledCheeseNaan.html')

def profile(request):
    return HttpResponse('<h1>Awesome profile view coming soon!</h1>')

def veganrecipes(request):
    return HttpResponse('<h1>I like vegan recipes.<h1>')

def recipes(request):
    return render(request, 'master_app/recipes.html')

def search(request):
    recipes = Recipe.objects.all()
    recipe_filter = RecipeFilter(request.GET, queryset=recipes)
    return render(request, 'master_app/recipe_list.html',{'filter':recipe_filter})
    #if request.POST:
      #  return render_to_response('master_app/search.html', {'result': google()})
        #return HttpResponseRedirect("/")
    #else:
        #return render_to_response('master_app/search.html')

def veg_search(request):
    return render(request, 'master_app/veg_search.html')   

def discover(request):
    return render(request, 'master_app/discover.html')

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
