from django.shortcuts import render
from django.shortcuts import  HttpResponse

def about(request):
    # return HttpResponse('about Page')
    return render(request, 'about.html')

def home(request):
    # return HttpResponse('<a href="/about">Go to about page</a>')
    return render(request, 'home.html')
