from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import Http404,HttpResponse, HttpResponseRedirect
#from websearch
from searchengine.web_search import google
from .forms import RecipeSearchForm
# Create your views here.

def search(request):
    if request.POST:
        return render_to_response('search.html', {'result': google()})
        #return HttpResponseRedirect("/")
    else:
        return render_to_response('search.html')

def recipe(request):
    form = RecipeSearchForm(request.GET)
    notes = form.search()
    return render_to_response('search.html', {'recipe': recipe})

def veg_search(request):
    return render(request, 'search/veg_search.html')