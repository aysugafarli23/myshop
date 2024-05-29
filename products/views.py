from django.shortcuts import render
from .models import Products

# Create your views here.
def home__page(request):
    products = Products.objects.all()
    return render (request, 'index.html',  {"products": products})

def about__view(request):
    return render(request, 'about.html' )

def contact__view(request):
    return render(request, 'contact.html')