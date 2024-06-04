from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Products, Comment
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
    keyword = request.GET.get("keyword")
    if keyword:
        products = Products.objects.filter(name__contains =keyword)
        return render(request, 'products.html', {"products": products})
    
    products = Products.objects.all()
    return render (request, 'products.html',  {"products": products})

@login_required(login_url="account:login")
def product__details__view(request,id):
    # product = Products.objects.filter(id = id).first()
    product = get_object_or_404(Products, id=id)
    comments = Comment.objects.filter(product=product)
    
    context = {
        "product": product,
        "comments":comments
    }
    
    return render(request, 'productdetails.html', context)

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

@login_required(login_url="account:login")
def addcomment__view(request, id):
    product = get_object_or_404(Products, id=id)
    
    if request.method =="POST":
        comment_author = request.POST.get('comment_author')
        comment_content = request.POST.get('comment_content')
        
        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.product = product
        newComment.save()
        messages.success(request, "Reyiniz elave olundu...")
        
    return redirect(reverse("product-details", kwargs={"id":id}))
    
    
     