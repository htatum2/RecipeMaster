from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import Http404,HttpResponse, HttpResponseRedirect
#from websearch
from searchengine.web_search import google
# Create your views here.

def search(request):
    if request.POST:
        return render_to_response('search.html', {'result': google()})
        #return HttpResponseRedirect("/")
    else:
        return render_to_response('search.html')
