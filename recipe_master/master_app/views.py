from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from .forms import RecipeForm, ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Recipe, Review
from django.db.models import Avg
from .filters import RecipeFilter
from django.core.exceptions import PermissionDenied
from django.shortcuts import Http404,HttpResponse, HttpResponseRedirect
#from searchengine.web_search import google
from django.contrib.auth.decorators import login_required
import operator
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.db.models import Q
from functools import reduce
import datetime
from django.db.models import Avg

# Create your views here.
# Class based views look for <app>/<model>_<viewtype>.html by default

def home(request):
    return render(request, 'master_app/home.html')

class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    success_url = '/discover/'
    fields = ['recipe_name',
             'country',
             'calories',
             'category', 
             'ingredients_list',
             'instructions', 
             'description',
             'image', 
             'image2',
             'meal_PrepTime_Minutes']

    def form_valid(self, form):
        form.instance.recipe_creator = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    success_url = '/discover/'
    fields = ['recipe_name',
             'country',
             'calories', 
              'ingredients_list',
              'instructions',
              'description', 
              'category',
              'image', 
              'meal_PrepTime_Minutes']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('redirect'))

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.recipe_creator:
            return True
        return False

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/'

    def test_func(self):
            recipe = self.get_object()
            if self.request.user == recipe.recipe_creator:
                return True
            return False

@login_required
def review(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if Review.objects.filter(recipe=recipe, user=request.user).exists():
        Review.objects.get(recipe=recipe, user=request.user).delete()
    valid_review = Review(
        rating=request.POST['rating'],
        authenticityRating=request.POST['authenticityRating'],
        comment=request.POST['comment'],
        user=request.user,
        recipe=recipe)
    valid_review.save()
    #return HttpResponseRedirect(reverse('master_app:recipe_detail', args=(recipe_id,)))



def about(request):
    recipe3= Recipe.objects.order_by('recipe_name')
    users = Review.objects.order_by('user')
    avg = Review.objects.aggregate(overall_rating = Avg('rating'), authenticityRating = Avg('authenticityRating'))
    dict = {'records': recipe3, 'users': users, 'avg':avg}
    return render(request, 'master_app/about.html', context = dict)

def recipe_list(request):
    #recipes = Recipe.objects.all()
    recipes = Recipe.objects.order_by('recipe_name').annotate(
    average_rating=Avg('review__rating'), authenticity=Avg('review__authenticityRating'),
)
    recipe_filter = RecipeFilter(request.GET, queryset=recipes)
    return render(request, 'master_app/recipe_list.html',{'filter':recipe_filter})

def review_list(request):
    latest_review_list = Review.objects.order_by('-date')[:9]
    context = {'latest_review_list': latest_review_list}
    return render(request, 'master_app/review_list.html', context)

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'master_app/review_detail.html', {'review':review})

@login_required
def add_review(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        authenticityRating = form.cleaned_data['authenticityRating']
        comment = form.cleaned_data['comment']
        user = form.cleaned_data['user']
        review = Review()
        review.recipe = recipe
        review.user = user
        review.rating = rating
        review.authenticityRating = authenticityRating
        review.comment = comment
        review.date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('master_app:recipe_detail', args=(recipe.id,)))
        return HttpResponseRedirect(reverse('recipe-detail', args=(recipe.id,)))
    return render(request, 'master_app/recipe_detail.html', {'recipe': recipe, 'form': form})

def user_review_list(request, username=None):
    if not username:
        username=request.user.username
    latest_review_list = Review.objects.filter(user=username).orderby('-date')
    context = {'latest_review_list':latest_review_list, 'username':username}
    return render(request, 'master_app/review_list.html', context)