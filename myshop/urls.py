"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from  products.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home__page, name="home"),
    path("about/", about__view, name = "about"),
    path("contact/", contact__view, name ="contact"),
    path("account/", include('account.urls')),
    path("products/", products__view, name="products"),
    path("product-details/<int:id>", product__details__view, name="product-details"),
    path("addproduct/", addproducts__view, name="addproduct"),
    path("update/<int:id>", updateproducts__view, name="update"),
    path("delete/<int:id>", deleteproducts__view, name="delete"),
    path("comment/<int:id>", addcomment__view, name="addcomment"),
    path("dashboard/", dashboard__view, name="dashboard"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
   
    
]

handler404 = 'products.views.custom_404'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)