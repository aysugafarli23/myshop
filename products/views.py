from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from .forms import ProductsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def custom_404(request, exception):
    return render(request, '404.html', status=404)


def home__page(request):
    return render (request, 'index.html')


def about__view(request):
    messages.info(request, "Sayta daxil olmaq üçün qeydiyyatdan keçməlisiniz!")
    return render(request, 'about.html' )


def contact__view(request):
    messages.info(request, "Sayta daxil olmaq üçün qeydiyyatdan keçməlisiniz!")
    return render(request, 'contact.html')


@login_required(login_url = "account:login")
def products__view(request):
    products = Products.objects.all()
    context = {"products": products}
    return render (request, 'products.html',  context)

@login_required(login_url="account:login")
def addproducts__view(request):
    form = ProductsForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        product = form.save(commit=False)
        product.company = request.user
        product.save()
        
        messages.success(request, "Mehsulunuz uğurla əlavə olundu)")
        return redirect("dashboard")
    
    context = {"form": form}
    return render(request, "addproduct.html", context)


@login_required(login_url="account:login")
def updateproducts__view(request, id):
    product = get_object_or_404(Products, id=id)
    form = ProductsForm(request.POST or None, request.FILES or None, instance=product)
    
    if form.is_valid():
        product.save()
        messages.success(request,"Mehsul yeniden deyisdirildi")
        return redirect("dashboard")
    
    context = {"form":form}
    return render(request,"updates.html",context)


@login_required(login_url="account:login")
def deleteproducts__view(request,id):
    product = get_object_or_404(Products, id=id)
    product.delete()
    messages.success(request,"Mehsulunuz silindi")
    return redirect("dashboard")
    

@login_required(login_url="account:login")
def dashboard__view(request):
    products = Products.objects.filter(company = request.user)
    context = {"products": products}
    return render(request, "dashboard.html",context)