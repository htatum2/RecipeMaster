from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'master_app/home.html')

def about(request):
    return render(request, 'master_app/about.html')

def search(request):
    return HttpResponse('<h1>Awesome searching results coming soon!</h1>')

def profile(request):
    return HttpResponse('<h1>Awesome profile view coming soon!</h1>')