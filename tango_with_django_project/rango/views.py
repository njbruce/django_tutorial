#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("""Rango says hey there world! 
        <br/>See the <a href='/rango/about'>About</a> page.""")

def about(request):
    return HttpResponse("""Rango says here is the about page.
        <br/> To go back to the index page 
        click <a href='/rango/'>here</a>.""")

