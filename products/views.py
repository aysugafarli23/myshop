from django.shortcuts import render
from .models import Products
from django.contrib import messages

# Create your views here.
def home__page(request):
    products = Products.objects.all()
    return render (request, 'index.html',  {"products": products})

def about__view(request):
    messages.info(request, "Sayta daxil olmaq üçün qeydiyyatdan keçməlisiniz!")
    return render(request, 'about.html' )

def contact__view(request):
    messages.info(request, "Sayta daxil olmaq üçün qeydiyyatdan keçməlisiniz!")
    return render(request, 'contact.html')