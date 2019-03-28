from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Recipe
from django.shortcuts import Http404,HttpResponse, HttpResponseRedirect
from searchengine.web_search import google
#from websearch

# Create your views here.

def home(request):
    context = {
        #'recipes': Recipe.objects.all()
    }
    return render(request, 'master_app/home.html', context)

def about(request):
    return render(request, 'master_app/about.html')

# def search(request):
#    return HttpResponse('<h1>Awesome searching results coming soon!</h1>')

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
    return render(request, 'veg_search.html')       
        